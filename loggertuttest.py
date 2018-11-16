import logging
import coloredlogs
import sys

def make_log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    file_handler = logging.FileHandler("mylogs.log")
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    coloredlogs.install(level='INFO')
    
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")



if __name__ == "__main__":
    make_log()
