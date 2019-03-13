import json

import requests
from django.test import TestCase
from rest_framework import status

from .views import user_post


class PostTest(TestCase):

    def test_good_post_request(self):
        url = 'http://127.0.0.1:8000/posts'

        payload = {
            "title": "your title",
            "content": "your content"
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT <token>"
        }

        request = requests.post(url, data=json.dumps(payload), headers=headers)

        self.assertIs(user_post(request), status.HTTP_201_CREATED)

    def test_fail_post_request(self):
        url = 'http://127.0.0.1:8000/posts'

        payload = {
            "wrong title": "title",
            "content": "content"
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT <token>"
        }

        request = requests.post(url, data=json.dumps(payload), headers=headers)

        self.assertIs(user_post(request), status.HTTP_409_CONFLICT)

    def text_good_put_request(self):
        url = 'http://127.0.0.1:8000/posts'

        payload = {
            "title": "my created post",
            "like": "True"
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT <token>"
        }

        request = requests.put(url, data=json.dumps(payload), headers=headers)

        self.assertIs(user_post(request), status.HTTP_200_OK)

    def test_good_get_request(self):
        url = 'http://127.0.0.1:8000/posts'

        payload = {
            "title": "my created post"
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT <token>"
        }

        request = requests.get(url, data=json.dumps(payload), headers=headers)

        self.assertIs(user_post(request), status.HTTP_200_OK)
