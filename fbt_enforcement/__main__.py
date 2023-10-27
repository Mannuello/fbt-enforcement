from .data_tools import get_all_car_data_records, get_random_plate_path_from_directory
from .plate_reader import get_single_car_data, read_plate_from_image

if __name__ == "__main__":
    plate_path = get_random_plate_path_from_directory()
    plate_number = read_plate_from_image(plate_path)
    all_car_records = get_all_car_data_records()
    car_record = get_single_car_data(plate_number, all_car_records)
