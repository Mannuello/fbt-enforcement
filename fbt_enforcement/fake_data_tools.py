import os
import random
import logging
from faker import Faker

logger = logging.getLogger(__name__)


def fake_plate_data():
    fake = Faker()
    logger.info("Mock API call retrieved all car data records")
    plate_numbers = ["HG54HA", "HYM945P", "VCP2429", "GRG29TA"]
    return [
        {
            "plate_number": plate,
            "owner": {
                "name": fake.name(),
                "address": fake.address(),
                "phone": fake.phone_number(),
                "email": fake.ascii_email(),
            },
            "vehicle": {
                "make": random.choice(["Toyota", "Honda", "Ford", "Telsa"]),
                "model": random.choice(["Civic", "Accord", "CR-V", "Pilot"]),
                "year": fake.year(),
                "color": fake.color_name(),
                "vin": fake.vin(),
            },
            "miles_per_hour": fake.random_int(min=50, max=100),
        }
        for plate in plate_numbers
    ]


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
