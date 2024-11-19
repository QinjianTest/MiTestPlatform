# core/config/logger_setup.py
# 日志配置
import logging
from logging.handlers import TimedRotatingFileHandler
import os

def setup_logging():
    # 确保 logs 目录存在
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # 创建一个处理器，每天生成一个新的日志文件
    handler = TimedRotatingFileHandler('logs/app.log', when='midnight', interval=1, backupCount=30)
    handler.setLevel(logging.DEBUG)  # 记录 DEBUG 及以上级别的日志

    # 设置格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)

    # 获取根日志记录器并添加处理器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    # 可选：添加一个控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
