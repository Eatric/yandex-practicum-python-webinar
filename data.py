CREATE_BOOKING_BODY = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

AUTH_BODY = {
    "username": "admin",
    "password": "password123"
}

def modify_firstname_booking_body(value):
    return modify_create_booking_body("firstname", value)


def modify_create_booking_body(key, value):
    new_body = CREATE_BOOKING_BODY.copy()
    new_body[key] = value

    return new_body
