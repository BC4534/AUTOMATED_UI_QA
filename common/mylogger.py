import logging
import os
import time
import sys

from common import all_file_path


class Logger(object):
    """
    Logger类用于封装日志功能，提供信息、调试、警告、错误和严重错误等不同级别的日志记录方法。
    """
    logs_file_path = os.path.join(all_file_path.project_path, "output", "logs")  # 定义日志文件存放路径

    def __init__(self, name="test_case_log", log_file=None):
        """
        初始化Logger类实例。

        Parameters:
            name: 日志记录器的名称，默认为"test_case_log"。
            log_file: 日志文件的路径，默认为None。
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # 设置日志级别

        # 如果日志目录不存在，则创建日志目录
        if not os.path.exists(Logger.logs_file_path):
            os.makedirs(Logger.logs_file_path)

        # 如果未指定日志文件名，则根据当前日期生成日志文件名
        if log_file is None:
            log_file = os.path.join(Logger.logs_file_path, time.strftime('%Y_%m_%d', time.localtime(time.time())) + ".log")

        # 移除已有的处理器
        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)

        try:
            # 创建文件处理器，用于将日志写入到指定的文件中
            self.file_handler = logging.FileHandler(log_file, encoding='utf-8')
            self.file_handler.setLevel(logging.DEBUG)

            # 创建控制台处理器，用于在控制台输出日志信息
            self.console_handler = logging.StreamHandler(sys.stdout)
            self.console_handler.setLevel(logging.INFO)

            # 创建一个日志格式器，定义日志信息的格式和日期格式
            formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                                          datefmt="%Y-%m-%d %H:%M:%S")

            # 将格式器设置给文件处理器和控制台处理器
            self.file_handler.setFormatter(formatter)
            self.console_handler.setFormatter(formatter)

            # 将文件处理器和控制台处理器添加到日志记录器中
            self.logger.addHandler(self.file_handler)
            self.logger.addHandler(self.console_handler)

        except Exception as e:
            print(f"Error setting up log handlers: {e}")

    def critical(self, msg):
        self.logger.critical(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def error(self, msg):
        self.logger.error(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)


# 主程序执行块，用于测试Logger类的功能
if __name__ == '__main__':
    # # logger = Logger(    )
    # logger.info("这是一个info测试日志")
    # logger.debug("这是一个debug测试日志")
    # logger.warning("这是一个warning测试日志")
    # logger.error("这是一个error测试日志")
    # logger.critical("这是一个critical测试日志")
    pass

