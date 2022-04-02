import errno
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter
import time

logger = logging.getLogger(__name__)


class LogConfig:
    configs_dict = {}

    def __init__(self, configs_dict):
        self.configs_dict = configs_dict

    def configure_log(self):
        self.create_dir()
        self.configure()

    def create_dir(self):
        try:
            if not os.path.exists('logs'):
                os.makedirs('logs')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def configure(self):
        log_file = 'logs/log.' + time.strftime('%Y%m%d') + '.log'
        if self.configs_dict.get('log_max_days') == 0:
            max_days = '30'
        else:
            max_days = self.configs_dict.get('log_max_days')

        # self.logger = logging.getLogger(__name__)
        handler = TimedRotatingFileHandler(filename=log_file, when='D', interval=int(max_days), encoding='utf-8')
        formatter = Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        self.set_log_level(logging)

    def set_log_level(self, _logging):
        if self.configs_dict.get('log_level') == 0:
            log_level = 1
        else:
            log_level = int(self.configs_dict.get('log_level'))

        if log_level == 1:
            logger.setLevel(_logging.ERROR)
        elif log_level == 2:
            logger.setLevel(_logging.WARNING)
        elif log_level == 3:
            logger.setLevel(_logging.INFO)
        elif log_level == 4:
            logger.setLevel(_logging.DEBUG)
        else:
            logger.setLevel(_logging.ERROR)

    def get_logger(self):
        return logger
