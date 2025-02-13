# 3p
# project
import wrapt

import ddtrace

# keep the TracedMongoClient import to avoid breaking the public api
from ddtrace.contrib.internal.pymongo.client import TracedMongoClient  # noqa: F401
from ddtrace.ext import mongo as mongox
from ddtrace.internal.schema import schematize_service_name


# TODO(Benjamin): we should instrument register_connection instead, because more generic
# We should also extract the "alias" attribute and set it as a meta
_SERVICE = schematize_service_name(mongox.SERVICE)


# TODO(mabdinur): Remove this class when ``ddtrace.contrib.mongoengine.trace`` is removed
class WrappedConnect(wrapt.ObjectProxy):
    """WrappedConnect wraps mongoengines 'connect' function to ensure
    that all returned connections are wrapped for tracing.
    """

    def __init__(self, connect):
        super(WrappedConnect, self).__init__(connect)
        ddtrace.trace.Pin(_SERVICE).onto(self)

    def __call__(self, *args, **kwargs):
        client = self.__wrapped__(*args, **kwargs)
        pin = ddtrace.trace.Pin.get_from(self)
        if pin:
            # Calling ddtrace.pin.Pin(...) with the `tracer` argument generates a deprecation warning.
            # Remove this if statement when the `tracer` argument is removed
            if pin.tracer is ddtrace.tracer:
                ddtrace.trace.Pin(service=pin.service).onto(client)
            else:
                ddtrace.trace.Pin(service=pin.service, tracer=pin.tracer).onto(client)

        return client
