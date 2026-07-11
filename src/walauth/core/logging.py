import logging
import sys

def setup_logging(is_dev: bool) -> None:
    handler = logging.StreamHandler(sys.stdout)
    if is_dev:
        fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    else:
        # JSON-ish for log aggregators; swap for python-json-logger if you want strict JSON
        fmt = '{"time":"%(asctime)s","level":"%(levelname)s","logger":"%(name)s","message":"%(message)s"}'
    handler.setFormatter(logging.Formatter(fmt))

    root = logging.getLogger()
    root.setLevel(logging.DEBUG if is_dev else logging.INFO)
    root.handlers = [handler]

    # quiet noisy third-party loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING if not is_dev else logging.INFO)