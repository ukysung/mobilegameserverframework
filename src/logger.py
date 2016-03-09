
import logging
import logging.handlers

import g

def get_log_level():
    if g.CFG['log']['level'] == 'debug':
        return logging.DEBUG
    elif g.CFG['log']['level'] == 'info':
        return logging.INFO
    elif g.CFG['log']['level'] == 'warn':
        return logging.WARNING
    elif g.CFG['log']['level'] == 'error':
        return logging.ERROR
    else:
        return logging.DEBUG

def get_log_rotation():
    if g.CFG['log']['rotation'] == 'every_minute':
        return 'M'
    elif g.CFG['log']['rotation'] == 'hourly':
        return 'H'
    elif g.CFG['log']['rotation'] == 'daily':
        return 'D'
    else:
        return 'M'

def init(server_type, server_seq):
    log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
    log_handler = logging.handlers.TimedRotatingFileHandler(
        '../log/' + server_type + '_server_' + server_seq + '.csv',
        when=get_log_rotation(), interval=1)
    log_handler.setFormatter(log_formatter)

    g.LOG = logging.getLogger()
    g.LOG.setLevel(get_log_level())
    g.LOG.addHandler(log_handler)

