#!/usr/bin/env python3
from unittest import TestCase
from public.script import calculate_factorial

class MyTests(TestCase):

    def test_negative_str_invalida(self):
        with self.assertRaises(ValueError):
            calculate_factorial("-10")

    def test_cero(self):
        expected = 1
        actual = calculate_factorial(0)
        self.assertEqual(expected,actual)

    def test_none(self):
        expected = None
        actual = calculate_factorial(None)
        self.assertEqual(expected,actual)

    def test_cinco_str(self):
        expected = 120
        actual = calculate_factorial("5")
        self.assertEqual(expected,actual)

    def test_string_invalid(self):
        with self.assertRaises(TypeError):
            calculate_factorial("gfedcba")

    def test_big_str_invalid(self):
        with self.assertRaises(ValueError):
            calculate_factorial("21")

    def test_big(self):
        with self.assertRaises(ValueError):
            calculate_factorial(15)
