import os
import random
import logging
from typing import Any

from .fake_car_data import car_data


logger = logging.getLogger(__name__)


def fake_car_data() -> list[dict[str, Any]]:
    """Returns all car records"""
    logger.info("Mock API call retrieved all car data records")
    return car_data


def fake_plate_asset_path() -> str:
    """Returns a random plate image path from a directory of 4 plate images"""
    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.relpath(__file__))

    # Define the relative path to the "plates" directory
    directory_path = os.path.join(script_dir, "plates")

    image_files = [file for file in os.listdir(directory_path) if file.endswith(".png")]
    if plate_path_choice := random.choice(image_files + [None]):
        plate_path = os.path.normpath(os.path.join(directory_path, plate_path_choice))
        logger.info(f"Mock random plate path: {plate_path}")
        return plate_path
    else:
        logger.info("Mock random plate path: None")
        return None
