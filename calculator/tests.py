from django.test import TestCase, Client
from django.urls import reverse

class CalculatorTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_addition(self):
        response = self.client.post(reverse('calculate'), {
            'number_one': '10',
            'number_two': '5',
            'operation': 'add'
        })
        self.assertContains(response, '15')

    def test_subtraction(self):
        response = self.client.post(reverse('calculate'), {
            'number_one': '10',
            'number_two': '5',
            'operation': 'subtract'
        })
        self.assertContains(response, '5')

    def test_multiplication(self):
        response = self.client.post(reverse('calculate'), {
            'number_one': '10',
            'number_two': '5',
            'operation': 'multiply'
        })
        self.assertContains(response, '50')

    def test_division(self):
        response = self.client.post(reverse('calculate'), {
            'number_one': '10',
            'number_two': '5',
            'operation': 'divide'
        })
        self.assertContains(response, '2')

    def test_invalid_operation(self):
        response = self.client.post(reverse('calculate'), {
            'number_one': '10',
            'number_two': '5',
            'operation': 'invalid'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'calculator.html')
