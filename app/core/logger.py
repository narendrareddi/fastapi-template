import os
from logging.config import dictConfig

def setup_logging():
    """
    Sets up application-wide logging configuration.
    This function creates a 'logs' directory in the current working directory if it does not exist,
    and configures the logging system to output logs both to the console and to a file ('logs/app.log').
    The log format includes the timestamp, log level, logger name, and message.
    The root logger is set to the INFO level.
    Inline comments:
        - Creates 'logs/' directory if it doesn't exist.
        - Defines logging configuration with formatters, handlers (console and file), and root logger.
        - Applies the configuration using dictConfig.
    """
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)  # ✅ Create logs/ if it doesn't exist
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "logs/app.log",
                "formatter": "default",
                "mode": "a",
            },
        },
        "root": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
    }

    dictConfig(logging_config)
