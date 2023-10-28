from fbt_enforcement.plate_reader import get_single_car_data, read_plate_from_image


def test_read_plate_from_image():
    plate_1 = read_plate_from_image("fbt_enforcement/plates/euro_plate_1.png")
    plate_2 = read_plate_from_image("fbt_enforcement/plates/euro_plate_2.png")
    plate_3 = read_plate_from_image("fbt_enforcement/plates/euro_plate_3.png")
    plate_4 = read_plate_from_image("fbt_enforcement/plates/euro_plate_4.png")

    assert plate_1 == "HG54HA"
    assert plate_2 == "HYM945P"
    assert plate_3 == "VCP2429"
    assert plate_4 == "GRG29TA"


def test_get_single_car_data(fake_car_data):
    car_data = get_single_car_data("HG54HA", fake_car_data)
    assert car_data["owner"]["name"] == "John Doe"

    car_data = get_single_car_data("HYM945P", fake_car_data)
    assert car_data["vehicle"]["make"] == "Honda"

    car_data = get_single_car_data("VCP2429", fake_car_data)
    assert car_data["miles_per_hour"] == 85

    no_car_data = get_single_car_data("NULL", fake_car_data)
    assert no_car_data == {}
