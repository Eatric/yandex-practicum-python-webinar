import booking
import data


TOKEN = booking.get_token()


def test_success_delete_booking():
    # Arrange
    created_booking_id = booking.create_booking(data.CREATE_BOOKING_BODY).json()["bookingid"]

    # Act
    deleted_booking_result = booking.delete_booking(created_booking_id, TOKEN)

    # Assert
    assert deleted_booking_result.status_code == 201,\
        f"Expected 201, but actual is {deleted_booking_result.status_code}"


def test_success_delete_booking_with_custom_firstname():
    # Arrange
    created_body = data.modify_firstname_booking_body("Kamil")
    created_booking_id = booking.create_booking(created_body).json()["bookingid"]

    # Act
    deleted_booking_result = booking.delete_booking(created_booking_id, TOKEN)

    # Assert
    assert deleted_booking_result.status_code == 201,\
        f"Expected 201, but actual is {deleted_booking_result.status_code}"