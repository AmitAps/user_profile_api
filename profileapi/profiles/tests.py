import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile


class RegistrationTest(APITestCase):
    def test_registration(self):
        data = {'username': 'testcase', 'email': 'aps@mail.com', 'password': 'some_strong_password', 'password2': 'some_strong_password'}

        response = self.client.post('')
