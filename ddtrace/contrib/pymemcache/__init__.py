"""Instrument pymemcache to report memcached queries.

``import ddtrace.auto`` will automatically patch the pymemcache ``Client``::

    from ddtrace import patch
    from ddtrace.trace import Pin

    # If not patched yet, patch pymemcache specifically
    patch(pymemcache=True)

    # Import reference to Client AFTER patching
    import pymemcache
    from pymemcache.client.base import Client

    # Use a pin to specify metadata related all clients
    Pin.override(pymemcache, service='my-memcached-service')

    # This will report a span with the default settings
    client = Client(('localhost', 11211))
    client.set("my-key", "my-val")

    # Use a pin to specify metadata related to this particular client
    Pin.override(client, service='my-memcached-service')

    # If using a HashClient, specify metadata on each of its underlying
    # Client instances individually
    client = HashClient(('localhost', 11211))
    for _c in client.clients.values():
        Pin.override(_c, service="my-service")

Pymemcache ``HashClient`` will also be indirectly patched as it uses ``Client``
under the hood.
"""


# Required to allow users to import from  `ddtrace.contrib.pymemcache.patch` directly
import warnings as _w


with _w.catch_warnings():
    _w.simplefilter("ignore", DeprecationWarning)
    from . import patch as _  # noqa: F401, I001

from ddtrace.contrib.internal.pymemcache.patch import get_version  # noqa: F401
from ddtrace.contrib.internal.pymemcache.patch import patch  # noqa: F401
from ddtrace.contrib.internal.pymemcache.patch import unpatch  # noqa: F401
