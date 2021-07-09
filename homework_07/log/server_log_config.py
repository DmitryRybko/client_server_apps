import logging

logging.basicConfig(
    filename="log/server.log",
    format="%(asctime)s %(levelname)-10s %(module)s %(message)s",
    level=logging.INFO
)
