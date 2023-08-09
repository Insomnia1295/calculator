from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestCalculatorAPI:

    @classmethod
    def setup_class(cls):
        cls.api_client = APIClient()

    def test_addition(self):
        url = reverse('api-calculator')
        data = {
            'number1': 5,
            'number2': 10,
            'function': '+',
        }
        response = self.api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['result'] == 15

    def test_subtraction(self):
        url = reverse('api-calculator')
        data = {
            'number1': 15,
            'number2': 7,
            'function': '-',
        }
        response = self.api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['result'] == 8

    def test_multiplication(self):
        url = reverse('api-calculator')
        data = {
            'number1': 4,
            'number2': 6,
            'function': '*',
        }
        response = self.api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['result'] == 24

    def test_division(self):
        url = reverse('api-calculator')
        data = {
            'number1': 20,
            'number2': 5,
            'function': '/',
        }
        response = self.api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['result'] == 4

    def test_division_by_zero(self):
        url = reverse('api-calculator')
        data = {
            'number1': 5,
            'number2': 0,
            'function': '/',
        }
        response = self.api_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['error'] == 'Cannot divide by zero'

    def test_invalid_function(self):
        url = reverse('api-calculator')
        data = {
            'number1': 10,
            'number2': 5,
            'function': 'invalid',
        }
        response = self.api_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['error'] == 'Invalid function'
