from fbt_enforcement.car_data_fetcher import get_single_car_data


def test_get_single_car_data(fake_car_data: list) -> None:
    car_data = get_single_car_data("HG54HA", fake_car_data)
    assert car_data["owner"]["name"] == "John Doe"

    car_data = get_single_car_data("HYM945P", fake_car_data)
    assert car_data["vehicle"]["make"] == "Honda"

    car_data = get_single_car_data("VCP2429", fake_car_data)
    assert car_data["miles_per_hour"] == 85

    no_car_data = get_single_car_data("NULL", fake_car_data)
    assert no_car_data is None
