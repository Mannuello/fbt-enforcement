from fbt_enforcement.plate_reader import read_plate_from_image


def test_read_plate_from_image() -> None:
    plate_1 = read_plate_from_image("fbt_enforcement/plates/euro_plate_1.png")
    plate_2 = read_plate_from_image("fbt_enforcement/plates/euro_plate_2.png")
    plate_3 = read_plate_from_image("fbt_enforcement/plates/euro_plate_3.png")
    plate_4 = read_plate_from_image("fbt_enforcement/plates/euro_plate_4.png")
    assert plate_1 == "HG54HA"
    assert plate_2 == "HYM945P"
    assert plate_3 == "VCP2429"
    assert plate_4 == "GRG29TA"

    no_plate = read_plate_from_image(None)  #  type: ignore [arg-type]
    assert no_plate is None
