from pytest import fixture

from fbt_enforcement.fake_car_data import car_data


@fixture
def fake_car_data():
    return car_data
