import sys
import os
import warnings


LOADED_MODULES = frozenset(sys.modules.keys())

from ddtrace.internal.module import ModuleWatchdog


ModuleWatchdog.install()

# Ensure we capture references to unpatched modules as early as possible
import ddtrace.internal._unpatched  # noqa
from ._logger import configure_ddtrace_logger

# configure ddtrace logger before other modules log
configure_ddtrace_logger()  # noqa: E402

from .settings import _global_config as config


# Enable telemetry writer and excepthook as early as possible to ensure we capture any exceptions from initialization
import ddtrace.internal.telemetry  # noqa: E402

from ._monkey import patch  # noqa: E402
from ._monkey import patch_all  # noqa: E402
from .internal.compat import PYTHON_VERSION_INFO  # noqa: E402
from .internal.utils.deprecations import DDTraceDeprecationWarning  # noqa: E402
from ddtrace._trace.pin import Pin  # noqa: E402
from ddtrace._trace.span import Span  # noqa: E402
from ddtrace._trace.tracer import Tracer  # noqa: E402
from ddtrace.vendor import debtcollector
from .version import get_version  # noqa: E402


# TODO(mabdinur): Remove this once we have a better way to start the mini agent
from ddtrace.internal.serverless.mini_agent import maybe_start_serverless_mini_agent as _start_mini_agent

_start_mini_agent()

# DEV: Import deprecated tracer module in order to retain side-effect of package
# initialization, which added this module to sys.modules. We catch deprecation
# warnings as this is only to retain a side effect of the package
# initialization.
# TODO: Remove this in v3.0 when the ddtrace/tracer.py module is removed
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from .tracer import Tracer as _

__version__ = get_version()

# TODO: Deprecate accessing tracer from ddtrace.__init__ module in v4.0
if os.environ.get("_DD_GLOBAL_TRACER_INIT", "true").lower() in ("1", "true"):
    from ddtrace.trace import tracer  # noqa: F401

__all__ = [
    "patch",
    "patch_all",
    "Pin",
    "Span",
    "Tracer",
    "config",
    "DDTraceDeprecationWarning",
]


_DEPRECATED_TRACE_ATTRIBUTES = [
    "Span",
    "Tracer",
    "Pin",
]


def __getattr__(name):
    if name in _DEPRECATED_TRACE_ATTRIBUTES:
        debtcollector.deprecate(
            ("%s.%s is deprecated" % (__name__, name)),
            message="Import from ddtrace.trace instead.",
            category=DDTraceDeprecationWarning,
            removal_version="3.0.0",
        )

    if name in globals():
        return globals()[name]

    raise AttributeError("%s has no attribute %s", __name__, name)


def check_supported_python_version():
    if PYTHON_VERSION_INFO < (3, 8):
        deprecation_message = (
            "Support for ddtrace with Python version %d.%d is deprecated and will be removed in 3.0.0."
        )
        if PYTHON_VERSION_INFO < (3, 7):
            deprecation_message = "Support for ddtrace with Python version %d.%d was removed in 2.0.0."
        debtcollector.deprecate(
            (deprecation_message % (PYTHON_VERSION_INFO[0], PYTHON_VERSION_INFO[1])),
            category=DDTraceDeprecationWarning,
        )


check_supported_python_version()
