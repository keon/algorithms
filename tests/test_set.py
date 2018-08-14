from algorithms.set import (
    find_keyboard_row
)

import unittest

class TestFindKeyboardRow(unittest.TestCase):
    def test_find_keyboard_row(self):
        self.assertEqual(["Alaska", "Dad"],
                         find_keyboard_row(["Hello", "Alaska", "Dad", "Peace"]))
