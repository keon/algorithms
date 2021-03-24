from algorithms.streaming.misra_gries import (
    misras_gries,
)
from algorithms.streaming import (
    one_sparse
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

class TestOneSparse(unittest.TestCase):
    def test_one_sparse_correct(self):
        self.assertEqual(4,one_sparse([(4,'+'), (2,'+'),(2,'-'),(4,'+'),(3,'+'),(3,'-')]))
        self.assertEqual(2,one_sparse([(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+')]))


    def test_one_sparse_incorrect(self):
        self.assertEqual(None,one_sparse([(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(1,'+')])) #Two values remaining
        self.assertEqual(None,one_sparse([(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'-'),(2,'-'),(2,'-'),(2,'-')])) # No values remaining
        self.assertEqual(None,one_sparse([(2,'+'),(2,'+'),(4,'+'),(4,'+')])) # Bitsum sum of sign is inccorect
