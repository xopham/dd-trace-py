import sys
from typing import Callable
from typing import Text

from wrapt import FunctionWrapper

from ddtrace.appsec._common_module_patches import wrap_object
from ddtrace.appsec._iast._taint_tracking import OriginType
from ddtrace.appsec._iast._taint_tracking import origin_to_str
from ddtrace.appsec._iast._taint_tracking._taint_objects import taint_pyobject
from ddtrace.appsec._iast._taint_utils import taint_structure
from ddtrace.internal.logger import get_logger


log = get_logger(__name__)


def set_and_check_module_is_patched(module_str: Text, default_attr: Text = "_datadog_patch") -> bool:
    try:
        __import__(module_str)
        module = sys.modules[module_str]
        if getattr(module, default_attr, False):
            return False
        setattr(module, default_attr, True)
    except ImportError:
        pass
    return True


def set_module_unpatched(module_str: Text, default_attr: Text = "_datadog_patch"):
    try:
        __import__(module_str)
        module = sys.modules[module_str]
        setattr(module, default_attr, False)
    except ImportError:
        pass


def try_wrap_function_wrapper(module: Text, name: Text, wrapper: Callable):
    try:
        wrap_object(module, name, FunctionWrapper, (wrapper,))
    except (ImportError, AttributeError):
        log.debug("IAST patching. Module %s.%s not exists", module, name)


def _patched_dictionary(origin_key, origin_value, original_func, instance, args, kwargs):
    result = original_func(*args, **kwargs)

    return taint_structure(result, origin_key, origin_value, override_pyobject_tainted=True)


def _iast_instrument_starlette_url(wrapped, instance, args, kwargs):
    def path(self) -> str:
        return taint_pyobject(
            self.components.path,
            source_name=origin_to_str(OriginType.PATH),
            source_value=self.components.path,
            source_origin=OriginType.PATH,
        )

    instance.__class__.path = property(path)
    wrapped(*args, **kwargs)


def _iast_instrument_starlette_request(wrapped, instance, args, kwargs):
    def receive(self):
        """This pattern comes from a Request._receive property, which returns a callable"""

        async def wrapped_property_call():
            body = await self._receive()
            return taint_structure(body, OriginType.BODY, OriginType.BODY, override_pyobject_tainted=True)

        return wrapped_property_call

    # `self._receive` is set in `__init__`, so we wait for the constructor to finish before setting the new property
    wrapped(*args, **kwargs)
    instance.__class__.receive = property(receive)


async def _iast_instrument_starlette_request_body(wrapped, instance, args, kwargs):
    result = await wrapped(*args, **kwargs)

    return taint_pyobject(
        result, source_name=origin_to_str(OriginType.PATH), source_value=result, source_origin=OriginType.BODY
    )


def _iast_instrument_starlette_scope(scope):
    if scope.get("path_params"):
        try:
            for k, v in scope["path_params"].items():
                scope["path_params"][k] = taint_pyobject(
                    v, source_name=k, source_value=v, source_origin=OriginType.PATH_PARAMETER
                )
        except Exception:
            log.debug("IAST: Unexpected exception while tainting path parameters", exc_info=True)
