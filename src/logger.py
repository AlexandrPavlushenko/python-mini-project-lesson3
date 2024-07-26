import logging
import os


def setup_logging_masks():
    path = os.path.dirname(os.path.abspath(__file__))
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename=os.path.join(path, "../logs/package_masks.log"),
        filemode="w",
    )
    return logging.getLogger()


def setup_logging_utils():
    path = os.path.dirname(os.path.abspath(__file__))
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename=os.path.join(path, "../logs/package_utils.log"),
        filemode="w",
    )
    return logging.getLogger()
