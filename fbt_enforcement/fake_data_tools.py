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


def get_random_plate_path_from_directory() -> str:
    """Returns a random plate image path from a directory of 4 plate images"""

    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the relative path to the "plates" directory
    directory_path = os.path.join(script_dir, "plates")

    image_files = [file for file in os.listdir(directory_path) if file.endswith(".png")]

    plate_path = os.path.normpath(
        os.path.join(directory_path, random.choice(image_files))
    )
    logger.info(f"Mock random plate path: {plate_path}")

    return plate_path
