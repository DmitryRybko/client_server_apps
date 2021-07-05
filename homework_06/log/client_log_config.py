import logging
import functools

logging.basicConfig(
    filename="log/client.log",
    format="%(asctime)s %(levelname)-10s %(module)s %(message)s",
    level=logging.INFO
)
