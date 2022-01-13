from ._version import __version__
from ._version import version_info

from opentelemetry.instrumentation.tornado import TornadoInstrumentor


TornadoInstrumentor().instrument()
