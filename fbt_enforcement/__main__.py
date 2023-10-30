import logging
from fbt_enforcement.fake_data_tools import (
    fake_get_all_car_data_records,
    fake_get_random_plate_path_from_directory,
)
from fbt_enforcement.plate_reader import read_plate_from_image
from fbt_enforcement.car_data_fetcher import get_single_car_data


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("FBT Enforcement app initialized")
    plate_path = fake_get_random_plate_path_from_directory()
    if plate_number := read_plate_from_image(plate_path):
        all_car_records = fake_get_all_car_data_records()
        if car_record := get_single_car_data(plate_number, all_car_records):
            # TODO implement ticketing & address updating pdf mailing system
            logger.info(f"Processing plate number: {plate_number}")
