"""
The ``jinja2`` integration traces templates loading, compilation and rendering.
Auto instrumentation is available using the ``patch``. The following is an example::

    from ddtrace import patch
    from jinja2 import Environment, FileSystemLoader

    patch(jinja2=True)

    env = Environment(
        loader=FileSystemLoader("templates")
    )
    template = env.get_template('mytemplate.html')


The library can be configured globally and per instance, using the Configuration API::

    from ddtrace import config
    from ddtrace.trace import Pin

    # Change service name globally
    config.jinja2['service_name'] = 'jinja-templates'

    # change the service name only for this environment
    Pin.override(env, service='jinja-templates')

By default, the service name is set to None, so it is inherited from the parent span.
If there is no parent span and the service name is not overridden the agent will drop the traces.
"""

# Required to allow users to import from  `ddtrace.contrib.jinja2.patch` directly
import warnings as _w


with _w.catch_warnings():
    _w.simplefilter("ignore", DeprecationWarning)
    from . import patch as _  # noqa: F401, I001


from ddtrace.contrib.internal.jinja2.patch import get_version  # noqa: F401
from ddtrace.contrib.internal.jinja2.patch import patch  # noqa: F401
from ddtrace.contrib.internal.jinja2.patch import unpatch  # noqa: F401
