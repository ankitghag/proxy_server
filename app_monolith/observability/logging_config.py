
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from observability.request_context import request_id

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

## these will decide where does the log will go .
class LoggerFilter(logging.Filter):
    def __init__(self, logger_name):
        super().__init__()
        self.logger_name = logger_name

    def filter(self, record):
        return record.name == self.logger_name

class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.ERROR

class RequestIDFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id.get()
        return True


def create_handler(filename, level=logging.INFO, filters=None):

    handler = RotatingFileHandler(LOG_DIR / filename, maxBytes=5 * 1024 * 1024, backupCount=5)

    handler.setLevel(level)

    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(request_id)s | %(name)s | %(message)s"))

    handler.addFilter(RequestIDFilter())

    if filters:
        for log_filter in filters:
            handler.addFilter(log_filter)

    return handler


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        handlers=[create_handler( "error.log", level=logging.ERROR, filters=[ErrorFilter()] )],
        force=True
    )

    access_logger= logging.getLogger("access")
    access_logger.addHandler(
        create_handler(
            "access.log",
            filters=[LoggerFilter("access")]
        )
    )
    access_logger.setLevel(logging.INFO)
    access_logger.propagate = False

    proxy_logger = logging.getLogger("proxy")
    proxy_logger.addHandler(
        create_handler(
            "proxy.log",
            filters=[LoggerFilter("proxy")]
        )
    )
    proxy_logger.setLevel(logging.INFO)
    proxy_logger.propagate = True

