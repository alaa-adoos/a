from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Crypto

from django.urls import reverse

class CryptoTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_Crypto = Crypto.objects.create(
            name="rake",
            owner=testuser1,
            desc="Better for collecting leaves than a shovel.",
            rank=1
        )
        test_Crypto.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")




    def test_Cryptos_model(self):
        Crypto = Crypto.objects.get(id=1)
        actual_owner = str(Crypto.owner)
        actual_name = str(Crypto.name)
        actual_desc = str(Crypto.desc)
        actual_rank = (Crypto.rank)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_rank, 1)
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_desc, "Better for collecting leaves than a shovel."
        )

    def test_get_Crypto_list(self):
        url = reverse("crypto_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Cryptos = response.data
        self.assertEqual(len(Cryptos), 1)
        

    def test_auth_required(self):
        self.client.logout()
        url = reverse("crypto_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("crypto_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)