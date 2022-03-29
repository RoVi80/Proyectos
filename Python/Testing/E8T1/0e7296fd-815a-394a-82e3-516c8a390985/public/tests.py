#!/usr/bin/env python3
from unittest import TestCase
from public.script import fine_calculator

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class FineCalculatorTest(TestCase):
    def test_area_type(self):
        self.assertEqual("Invalid Area Type", fine_calculator(33, 45))

    def test_area_value(self):
        expected = "Invalid Area Value"
        actual = fine_calculator("hola", 80)
        self.assertEqual(expected, actual)

    def test_speed_type(self):
        expected = "Invalid Speed Type"
        actual = fine_calculator("motorway", "20")
        self.assertEqual(expected, actual)
	
    def test_speed_value(self):
        expected = "Invalid Speed Value"
        actual = fine_calculator("urban", -50)
        self.assertEqual(expected, actual)
	
    def test_urban_limit(self):
        expected = 0
        actual = fine_calculator("urban", 40)
        self.assertEqual(expected, actual)

    def test_express_limit(self):
        expected = 0
        actual = fine_calculator("expressway", 80)
        self.assertEqual(expected, actual)

    def test_motorway(self):
        actual = fine_calculator("motorway", 90)
        expected = 0
        self.assertEqual(expected, actual)

    def test_area_case(self):
        actual = fine_calculator("URBAN", 40)
        expected = "Invalid Area Value"
        self.assertEqual(expected, actual)

    def test_expressway(self):
        actual = fine_calculator("expressway", 119)
        self.assertEqual(289, actual)