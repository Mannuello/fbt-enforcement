import logging
from datetime import datetime
from collections import Counter
from fbt_enforcement.fake_data_tools import (
    fake_plate_data,
    fake_plate_asset_path,
)
from fbt_enforcement.plate_reader import read_plate_from_image
from fbt_enforcement.car_data_fetcher import get_single_car_record


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app_start_time = datetime.now()
    logger.info("FBT Enforcement app initialized")
    counter = Counter()

    # Generating fake data
    plate_img_path = fake_plate_asset_path()
    all_car_data = fake_plate_data()

    # Core App Logic
    if plate_number := read_plate_from_image(plate_img_path):
        counter["plate_image_reads"] += 1
        if car_record := get_single_car_record(plate_number, all_car_data):
            counter["car_record_retrievals"] += 1
            # TODO implement ticketing & address updating pdf mailing system
            logger.info(f"Processing plate number: {plate_number}")

    logger.info(f"Total plates read: {counter['plate_image_reads']}")
    logger.info(f"Total records retrieved: {counter['car_record_retrievals']}")

    app_end_time = datetime.now()
    logger.info(f"App started at {app_start_time}")
    logger.info(f"App ended at {app_end_time}")
    logger.info(f"Total runtime: {app_end_time - app_start_time}")
