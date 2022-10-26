import logging

log_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
}

logging.basicConfig(
    level="INFO",
    format="[%(asctime)s][%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler()],
    datefmt='%H:%M:%S'
)

def info(message):
    logging.info(message)

def debug(message):
    logging.debug(message)