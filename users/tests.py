import json

import requests
from django.test import TestCase
from rest_framework import status

from .views import User


class PostTest(TestCase):

    def test_good_post_request(self):
        url = 'http://127.0.0.1:8000/posts'

        payload = {
            "email": "nsheva@gmail.com",
            "first_name": "Nikolay",
            "last_name": "Shevchenko",
            "password": "sheva"
        }

        headers = {
            "Content-Type": "application/json"
        }

        request = requests.post(url, data=json.dumps(payload), headers=headers)

        self.assertIs(User(request), status.HTTP_201_CREATED)


    def test_fail_post_request(self):
        url = 'http://127.0.0.1:8000/posts'

        payload = {
            "email": "admin@gmail.com",
            "first_name": "Name",
            "last_name": "Surname",
            "password": "password"
        }

        headers = {
            "Content-Type": "application/json"
        }

        request = requests.post(url, data=json.dumps(payload), headers=headers)

        self.assertIs(User(request), status.HTTP_201_CREATED)
