# Testing locks

import requests
import threading

URL = 'http://127.0.0.1:8080/api/secure/ab/1/'

HEADER_1 = {'Authorization': 'Token 4ee135a22ca240bcf848a367fcadd54ee8918d21'}
HEADER_2 = {'Authorization': 'Token 1abb6b2da6cea59e38bcf9f387b10ccdd6ff7e6e'}


def get_request_1():
    r = requests.get(URL, headers=HEADER_1)
    print(r.text)


def get_request_2():
    r = requests.get(URL, headers=HEADER_2)
    print(r.text)


def main():
    first_thread = threading.Thread(target=get_request_1)

    second_thread = threading.Thread(target=get_request_2)
    first_thread.start()
    second_thread.start()

    return None