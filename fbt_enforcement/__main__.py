import logging
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
    logger.info("FBT Enforcement app initialized")

    # Generating fake data
    plate_img_path = fake_plate_asset_path()
    all_car_data = fake_plate_data()

    # Core App Logic
    if plate_number := read_plate_from_image(plate_img_path):
        if car_record := get_single_car_record(plate_number, all_car_data):
            # TODO implement ticketing & address updating pdf mailing system
            logger.info(f"Processing plate number: {plate_number}")
