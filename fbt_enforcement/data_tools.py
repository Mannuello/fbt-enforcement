import os
import random
from typing import Any

from .fake_car_data import car_data


def get_all_car_data_records() -> list[dict[str, Any]]:
    """Brett - Returns all car records"""
    print("Doing an API call to get all the car data in our system")
    return car_data


def get_random_plate_path_from_directory() -> str:
    """Brett - Returns a random plate image path from a directory of 4 plate images"""
    directory_path = "fbt_enforcement/plates"
    image_files = [
        file for file in os.listdir(directory_path) if file.endswith((".png"))
    ]
    return os.path.normpath(os.path.join(directory_path, random.choice(image_files)))
