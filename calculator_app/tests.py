from django.test import TestCase
from django.urls import reverse
from calculator_app.calculator import Calculator
from .models import Calculator
from .forms import CalculatorForm
from django.core.exceptions import ValidationError


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
