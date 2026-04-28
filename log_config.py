import logging


def get_logger(name: str = __name__) -> logging.Logger:
    ## -- Função simples de configuração de logger. -- ##

    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        datefmt='%Y-%m-%d %H:%M:%S',
        filename = 'app_log.log',
        filemode = 'a'
    )

    logger = logging.getLogger(name)
    return logger


if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Logger initialized")
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")