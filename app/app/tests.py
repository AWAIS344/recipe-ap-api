"""
Simple Test Case for add function
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add(self):
        self.assertEqual(calc.add(3, 8), 11)
    
    #TDD ( TEST DRIVEN DEVELOPMENT)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 11), 6)

