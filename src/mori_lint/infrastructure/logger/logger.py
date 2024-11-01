import logging


def configure_logger(log_level=logging.DEBUG) -> None:
    logger = logging.getLogger("__mori__")
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
