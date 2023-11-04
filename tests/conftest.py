from pytest import fixture

from fbt_enforcement.fake_data_tools import fake_plate_data


@fixture
def fake_car_data():
    return fake_plate_data()
