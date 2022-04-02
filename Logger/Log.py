from Logger import LogConfig


class Log:
    @staticmethod
    def get_logger():
        return LogConfig.logger
