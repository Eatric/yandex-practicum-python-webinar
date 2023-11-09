import pytest

import booking
import data


def test_success_create_booking():
    # Arrange
    # Act
    response = booking.create_booking(data.CREATE_BOOKING_BODY)

    # Assert
    assert response.status_code == 200

@pytest.mark.parametrize("firstname", [
    pytest.param("A", id="Check one symbol in firstName"),
    pytest.param("Kamil", id="Check normal name in firstName"),
    pytest.param("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                 id="Check Big Fistname")
])
def test_success_create_booking_with_custom_firstname(firstname):
    # Arrange
    body = data.modify_firstname_booking_body(firstname)

    # Act
    response = booking.create_booking(body)

    # Assert
    assert response.status_code == 200
    assert response.json()["booking"]["firstname"] == firstname
