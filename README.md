# calculator-web-app-
A simple calculator application built using Django. The application allows users to perform basic arithmetic operations like addition, subtraction, multiplication, and division.

## Features

- **Addition**: Add two numbers.
- **Subtraction**: Subtract one number from another.
- **Multiplication**: Multiply two numbers.
- **Division**: Divide one number by another.
- **Invalid Operation Handling**: Handles invalid operations gracefully.
  
## Installation
Running the project.......

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/subhash-negi/calculator-web-app-.git
   cd calculator-web-app-
   
2. **creating a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   
3. **install dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Run server**
   ```sh
   python manage.py runserver

Navigate to http://127.0.0.1:8000/ in your web browser to access the calculator application. Enter two numbers and select an operation to perform the calculation.


**TEST CASES**
The calculator app contains the following test cases that is run by the jenkins
```python
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
```

```markdown
     !(images/Screenshot 2024-07-15 175748.jpg)
     !(images/Screenshot 2024-07-15 175841.jpg)
```









