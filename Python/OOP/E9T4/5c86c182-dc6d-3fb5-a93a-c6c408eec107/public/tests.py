#!/usr/bin/env python3

from unittest import TestCase
from public.script import Matrix


class PublicTestSuite(TestCase):

    def assertFailedInit(self, A):
        with self.assertRaises(AssertionError) as ctx:
            A = Matrix(A)

    def test0_empty_list(self):
        self.assertFailedInit([])

    def test1_wrong_input(self):
        self.assertFailedInit("sdf")

    def test2_wrong_input(self):
        self.assertFailedInit(["sdf"])

    def test3_wrong_input(self):
        self.assertFailedInit([[]])

    def test4_wrong_input(self):
        self.assertFailedInit([["dd"]])

    def test5_wrong_input(self):
        self.assertFailedInit([1,2,3])

