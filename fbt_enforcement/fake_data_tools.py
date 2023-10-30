import os
import random
import logging
from typing import Any

from .fake_car_data import car_data

logger = logging.getLogger(__name__)


def fake_get_all_car_data_records() -> list[dict[str, Any]]:
    """Returns all car records"""
    logger.info("Mock API call retrieved all car data records")
    return car_data


def fake_get_random_plate_path_from_directory() -> str:
    directory_path = "fbt_enforcement/plates"
    image_files = [file for file in os.listdir(directory_path) if file.endswith(".png")]

    plate_path_choice = random.choice(image_files + [None])

    if plate_path_choice is None:
        logger.info("Mock random plate path is None")
        return None

    plate_path = os.path.normpath(os.path.join(directory_path, plate_path_choice))
    logger.info(f"Mock random plate path: {plate_path}")
    return plate_path
