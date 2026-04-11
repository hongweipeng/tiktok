import os
import time
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

logging.basicConfig(format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

if __name__ == '__main__':
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error msg: %s', 'tom')
    logger.critical('this is a logger critical message')
