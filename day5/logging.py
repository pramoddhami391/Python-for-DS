import logging
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s %(levelname)s %(message)s",
  filename="app.log",
  filemode="a"
)
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("Error message")
logging.critical("Critical message")