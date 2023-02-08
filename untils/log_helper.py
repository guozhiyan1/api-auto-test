import os
import logging.config

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def logger():
    # 是否保存日志文件
    is_save_log = False

    logging_config = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                # 自定义颜色
                "log_colors": {
                    'DEBUG': 'white',  # 自定义日志  ,bg_white
                    'INFO': 'green',
                    'WARNING': 'bold_yellow',
                    'ERROR': 'bold_red',
                    'CRITICAL': 'bold_purple'
                },
                # "format": "%(log_color)s[%(asctime)s] %(filenamefilename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s"
                "format": "%(log_color)s[%(asctime)s] -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "colored",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "my_module": {"level": "ERROR", "handlers": ["console"], "propagate": False}
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console"]
        },
    }
    if is_save_log:
        level = ['INFO', "DEBUG", "ERROR"]
        file_handler = ["info_file_handler", "debug_file_handler", "error_file_handler"]
        for i in range(3):
            logging_config['handlers'][file_handler[i]] = {
                "class": "logging.handlers.RotatingFileHandler",
                "level": level[i],
                "formatter": "colored",
                "filename": f"{base_path}/logs/{level[i]}.log",
                "maxBytes": 10485760,
                "backupCount": 50,
                "encoding": "utf-8"
            }
            logging_config['root']['handlers'].append(file_handler[i])
        # 初始化日志配置
    logging.config.dictConfig(logging_config)
    return logging
