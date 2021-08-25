from django.test import TestCase
import requests

ok = 200


def assert_correct_response(response, response_code, error_message=''):
    if response.status_code == response_code:
        assert True
    else:
        print(f'REQUEST:\n{response.url}\nFAILED')
        print(f'METHOD => {response.request.method}')
        print(f'ACTUAL RESULT: {response.status_code}')
        print(f'EXPECTED RESULT: {response_code}')
        print(response.json())
        if response.request.body:
            print(response.request.body.decode())
        assert False, error_message


class TestShop:
    def test_positive_response(self):
        url_for_test = requests.get('127.0.0.1/shop/')
        assert_correct_response(url_for_test, ok)

