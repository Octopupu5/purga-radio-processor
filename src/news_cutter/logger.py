import logging
from pathlib import Path

def get_logger(name='news_cutter', log_dir='logs', log_file='app.log'):
    Path(log_dir).mkdir(exist_ok=True)
    logger = logging.getLogger(f"{name}.{log_file}")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(Path(log_dir) / log_file, encoding='utf-8')
    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    if not any(isinstance(h, logging.FileHandler) and h.baseFilename == fh.baseFilename for h in logger.handlers):
        logger.addHandler(fh)
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        logger.addHandler(ch)
    return logger