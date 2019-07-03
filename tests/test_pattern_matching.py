from algorithms.pattern_matching import (
    bmh,
    bmhs,
    shift_and
)

import unittest

class TestSuite(unittest.TestCase):
  def test_bmh(self):
    self.assertEqual([6],bmh("I am Iron Man", "ro"))

  def test_bmhs(self):
    self.assertEqual([1, 3],bmhs("banana nanica", "ana"))
  
  def test_shift_and(self):
    self.assertCountEqual([5,18], shift_and("Drew dodd's dad's dog's dead", "do"))
