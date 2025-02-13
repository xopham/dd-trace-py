import azure.functions as azure_functions
from wrapt import wrap_function_wrapper as _w

from ddtrace import config
from ddtrace.contrib.internal.trace_utils import int_service
from ddtrace.contrib.internal.trace_utils import unwrap as _u
from ddtrace.ext import SpanTypes
from ddtrace.internal import core
from ddtrace.internal.schema import schematize_cloud_faas_operation
from ddtrace.internal.schema import schematize_service_name
from ddtrace.trace import Pin


config._add(
    "azure_functions",
    {
        "_default_service": schematize_service_name("azure_functions"),
    },
)


def get_version():
    # type: () -> str
    return getattr(azure_functions, "__version__", "")


def patch():
    """
    Patch `azure.functions` module for tracing
    """
    # Check to see if we have patched azure.functions yet or not
    if getattr(azure_functions, "_datadog_patch", False):
        return
    azure_functions._datadog_patch = True

    Pin().onto(azure_functions.FunctionApp)
    _w("azure.functions", "FunctionApp.route", _patched_route)


def _patched_route(wrapped, instance, args, kwargs):
    trigger = "Http"

    pin = Pin.get_from(instance)
    if not pin or not pin.enabled():
        return wrapped(*args, **kwargs)

    def _wrapper(func):
        function_name = func.__name__

        def wrap_function(req: azure_functions.HttpRequest, context: azure_functions.Context):
            operation_name = schematize_cloud_faas_operation(
                "azure.functions.invoke", cloud_provider="azure", cloud_service="functions"
            )
            with core.context_with_data(
                "azure.functions.patched_route_request",
                span_name=operation_name,
                pin=pin,
                service=int_service(pin, config.azure_functions),
                span_type=SpanTypes.SERVERLESS,
            ) as ctx, ctx.span:
                ctx.set_item("req_span", ctx.span)
                core.dispatch("azure.functions.request_call_modifier", (ctx, config.azure_functions, req))
                res = None
                try:
                    res = func(req)
                    return res
                finally:
                    core.dispatch(
                        "azure.functions.start_response", (ctx, config.azure_functions, res, function_name, trigger)
                    )

        # Needed to correctly display function name when running 'func start' locally
        wrap_function.__name__ = function_name

        return wrapped(*args, **kwargs)(wrap_function)

    return _wrapper


def unpatch():
    if not getattr(azure_functions, "_datadog_patch", False):
        return
    azure_functions._datadog_patch = False

    _u(azure_functions.FunctionApp, "route")
