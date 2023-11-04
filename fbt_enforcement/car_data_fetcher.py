import logging


logger = logging.getLogger(__name__)


def get_single_car_record(plate_number: str, car_records: list) -> dict | None:
    """Uses a plate number to find an associated car record and returns a single instance"""
    for record in car_records:
        if record.get("plate_number") == plate_number:
            logger.info(f"Single car record found with plate: {plate_number}")
            return record

    logger.info(f"Unable to find match with plate number: {plate_number}")
    return None
