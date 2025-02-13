"""
To trace the falcon web framework, install the trace middleware::

    import falcon
    from ddtrace import tracer
    from ddtrace.contrib.falcon import TraceMiddleware

    mw = TraceMiddleware(tracer, 'my-falcon-app')
    falcon.API(middleware=[mw])

You can also use the autopatching functionality::

    import falcon
    from ddtrace import tracer, patch

    patch(falcon=True)

    app = falcon.API()

To disable distributed tracing when using autopatching, set the
``DD_FALCON_DISTRIBUTED_TRACING`` environment variable to ``False``.

**Supported span hooks**

The following is a list of available tracer hooks that can be used to intercept
and modify spans created by this integration.

- ``request``
    - Called before the response has been finished
    - ``def on_falcon_request(span, request, response)``


Example::

    import ddtrace.auto
    import falcon
    from ddtrace import config

    app = falcon.API()

    @config.falcon.hooks.on('request')
    def on_falcon_request(span, request, response):
        span.set_tag('my.custom', 'tag')

:ref:`Headers tracing <http-headers-tracing>` is supported for this integration.
"""


# Required to allow users to import from  `ddtrace.contrib.falcon.patch` directly
import warnings as _w


with _w.catch_warnings():
    _w.simplefilter("ignore", DeprecationWarning)
    from . import patch as _  # noqa: F401, I001
from ddtrace.contrib.internal.falcon.middleware import TraceMiddleware
from ddtrace.contrib.internal.falcon.patch import get_version  # noqa: F401
from ddtrace.contrib.internal.falcon.patch import patch  # noqa: F401
from ddtrace.internal.utils.deprecations import DDTraceDeprecationWarning
from ddtrace.vendor.debtcollector import deprecate


def __getattr__(name):
    if name in ("patch", "get_version"):
        deprecate(
            ("%s.%s is deprecated" % (__name__, name)),
            message="Use ``import ddtrace.auto`` or the ``ddtrace-run`` command to configure this integration.",
            category=DDTraceDeprecationWarning,
            removal_version="3.0.0",
        )

    if name in globals():
        return globals()[name]
    raise AttributeError("%s has no attribute %s", __name__, name)


__all__ = ["TraceMiddleware"]
