from algorithms.streaming.misra_gries import (
    misras_gries,
)
import unittest

class TestMisraGreis(unittest.TestCase):
    def test_misra_correct(self):
        self.assertEqual({'4':5},misras_gries([1,4,4,4,5,4,4]))
        self.assertEqual({'1':4},misras_gries([0,0,0,1,1,1,1]))
        self.assertEqual({'0':4,'1':3},misras_gries([0,0,0,0,1,1,1,2,2],3))
        
    def test_misra_incorrect(self):
        self.assertEqual(None,misras_gries([1,2,5,4,5,4,4,5,4,4,5]))
        self.assertEqual(None,misras_gries([0,0,0,2,1,1,1]))
        self.assertEqual(None,misras_gries([0,0,0,1,1,1]))
    