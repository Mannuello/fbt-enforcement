from fbt_enforcement.car_data_fetcher import get_single_car_record


def test_get_single_car_record(fake_car_data: list) -> None:
    assert get_single_car_record("HG54HA", fake_car_data)
    assert get_single_car_record("HYM945P", fake_car_data)
    assert get_single_car_record("VCP2429", fake_car_data)
    assert get_single_car_record("GRG29TA", fake_car_data)
    no_car_data = get_single_car_record("NULL", fake_car_data)
    assert no_car_data is None
