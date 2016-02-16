#!/usr/bin/env python3

import logging, logging.handlers

log_handler = logging.handlers.TimedRotatingFileHandler('develop.log', when='M', interval=1)
log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
log_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handler)

logger.debug('1111 %s', 2)
