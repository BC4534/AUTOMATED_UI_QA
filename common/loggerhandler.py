import logging
from logging.handlers import RotatingFileHandler
import os
import datetime
import sys
from common.all_file_path import log_path


# 自定义日志过滤器类
class LogFilter(logging.Filter):
    """自定义日志过滤器，过滤掉INFO级别的日志"""

    def filter(self, record):
        # 过滤掉info级别的日志
        # return record.levelno != logging.INFO
        return True


# Logger类用于封装日志功能
class Logger:
    def __init__(
        self, name="运维系统UI测试日志", level=logging.DEBUG, log_dir=log_path
    ):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)  # 设置日志级别
        self.logger.addFilter(LogFilter())  # 添加自定义日志过滤器

        # 确保日志目录存在
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 创建包含日期的日志文件名
        log_filename = f"{log_dir}/{datetime.datetime.now().strftime('%Y-%m-%d')}.log"

        # 创建文件日志处理器，设置最大文件大小和备份文件数量，并指定编码为utf-8
        self.file_handler = RotatingFileHandler(
            log_filename, maxBytes=10485760, backupCount=5, encoding="utf-8"
        )
        self.file_handler.setLevel(level)  # 设置文件处理器的日志级别

        # 创建控制台日志处理器
        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setLevel(logging.INFO)
        # self.console_handler.setLevel(logging.WARNING)  # 设置控制台处理器的日志级别

        # 设置日志格式
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(threadName)s - %(message)s"
        )
        self.file_handler.setFormatter(formatter)  # 为文件处理器设置格式
        self.console_handler.setFormatter(formatter)  # 为控制台处理器设置格式

        # 只添加处理器一次
        if not self.logger.handlers:
            self.logger.addHandler(self.file_handler)
            self.logger.addHandler(self.console_handler)

    def get_logger(self):
        return self.logger


# 配置日志
logger = Logger().get_logger()

if __name__ == "__main__":
    # 测试不同级别的日志记录
    logger.debug("debug")  # 将被记录，因为级别低于DEBUG的不会被记录
    logger.info("info")  # 将不会被记录，因为INFO级别的日志被过滤器过滤掉了
    logger.warning("warning")  # 将被记录
    logger.error("error")  # 将被记录
    logger.critical("critical")  # 将被记录
