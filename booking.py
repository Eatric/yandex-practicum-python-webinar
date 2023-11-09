import requests

import configuration
import data


def create_booking(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_BOOKING_API_PATH, json=body)


def get_token():
    return create_token().json()["token"]


def create_token():
    return requests.post(configuration.BASE_URL + configuration.AUTH_BOOKING_API_PATH, json=data.AUTH_BODY)


def delete_booking(id, token):
    return requests.delete(configuration.BASE_URL + configuration.DELETE_BOOKING_API_PATH + str(id), headers={
        "Cookie": "token=" + token
        #"Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=" #+ get_token()
    })
