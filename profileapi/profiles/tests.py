import json
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'username': 'testcase', 'email': 'aps@mail.com', 'password1': 'APS_._2345', 'password2': 'APS_._2345'}

        response = self.client.post('/api/rest-auth/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    list_url = reverse("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(username="testcase", password="APS_._2345")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
