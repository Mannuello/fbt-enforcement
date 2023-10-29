import logging
from datetime import datetime
from fbt_enforcement.data_tools import (
    get_all_car_data_records,
    get_random_plate_path_from_directory,
)
from fbt_enforcement.plate_reader import get_single_car_data, read_plate_from_image

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("FBT Enforcement app initialized")
    plate_path = get_random_plate_path_from_directory()
    plate_number = read_plate_from_image(plate_path)
    all_car_records = get_all_car_data_records()
    car_record = get_single_car_data(plate_number, all_car_records)
