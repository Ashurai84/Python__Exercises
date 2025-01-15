#  110 .Write a script that uses the logging module to log debug, info, warning, and error messages to a file.

import logging

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_messages():
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")

# Example usage
log_file = "application.log"
setup_logging(log_file)
log_messages()
