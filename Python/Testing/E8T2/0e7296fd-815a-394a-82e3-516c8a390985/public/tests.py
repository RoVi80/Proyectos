#!/usr/bin/env python3
from unittest import TestCase
from public.script import move


class MoveTestSuite(TestCase):

    def test_move_left(self):
        state = (
            "######  ",
            "###    #",
            "#    o##",
            "    ####"
        )
        actual = move(state, "left")
        expected = (
            (
            "######  ",
            "###    #",
            "#   o ##",
            "    ####"
        ),
            ('left', 'right', 'up')
        )
        self.assertEqual(expected, actual)

    def test_move_down(self):
        state = (
            "######  ",
            "### o  #",
            "#     ##",
            "    ####"
        )
        actual = move(state, "down")
        expected = (
            (
            "######  ",
            "###    #",
            "#   o ##",
            "    ####"
            ),
            ("left", "right", "up")
        )
        self.assertEqual(expected, actual)
