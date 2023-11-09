import booking


def test_success_create_token():
    token = booking.create_token()

    assert token.status_code == 200
