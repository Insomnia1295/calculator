from django.test import TestCase
from django.urls import reverse
from calculator_app.calculator import Calculator
from .models import Calculator
from .forms import CalculatorForm
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
class CalculatorViewTest(TestCase):
    def test_calculator_addition(self):
        url = reverse('calculator')
        data= {
            'number1': 5,
            'number2': 10,
            'function': '+',
        }
        response= self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result: 15')
    
    def test_calculator_subtraction(self):
        url = reverse('calculator')
        data= {
            'number1': 5,
            'number2': 10,
            'function': '-',    
        }
        response= self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result: -5')
    
    def test_calculator_multiplication(self):
        url= reverse('calculator')
        data={
            'number1': 10,
            'number2': 2,
            'function': '*',
        }
        response= self.client.post(url,data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result: 20')

    def test_calculator_division(self):
        url= reverse('calculator')
        data={
            'number1': 10,
            'number2': 5,
            'function': '/',
        }
        response= self.client.post(url,data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result: 2')


class CalculatorAPITest(APITestCase):
    def test_addition(self):
        data = {
            'number1': 5,
            'number2': 10,
            'function': '+',
        }
        response = self.client.post(reverse('api-calculator'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 15)
        self.assertIsNone(response.data.get('error_message'))

    def test_subtraction(self):
        data = {
            'number1': 10,
            'number2': 3,
            'function': '-',
        }
        response = self.client.post(reverse('api-calculator'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 7)
        self.assertIsNone(response.data.get('error_message'))

    def test_multiplication(self):
        data = {
            'number1': 5,
            'number2': 4,
            'function': '*',
        }
        response = self.client.post(reverse('api-calculator'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 20)
        self.assertIsNone(response.data.get('error_message'))

    def test_division_by_zero(self):
        data = {
            'number1': 5,
            'number2': 0,
            'function': '/',
        }
        response = self.client.post(reverse('api-calculator'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNone(response.data.get('result'))
        self.assertEqual(response.data['error'], 'Cannot divide by zero')

    def test_invalid_function(self):
        data = {
            'number1': 10,
            'number2': 5,
            'function': 'invalid',
        }
        response = self.client.post(reverse('api-calculator'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNone(response.data.get('result'))
        self.assertEqual(response.data['error'], 'Invalid function')