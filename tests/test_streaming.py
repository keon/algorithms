 from algorithms.streaming import (
    one_sparse
)
import unittest   

class TestOneSparse(unittest.TestCase):
    def test_one_sparse_correct(self):
        self.assertEqual(4,one_sparse([(4,'+'), (2,'+'),(2,'-'),(4,'+'),(3,'+'),(3,'-')]))
        self.assertEqual(2,one_sparse([(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+')]))


    def test_one_sparse_incorrect(self):
        self.assertEqual(None,one_sparse([(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'+'),(1,'+')])) #Two values remaining
        self.assertEqual(None,one_sparse([(2,'+'),(2,'+'),(2,'+'),(2,'+'),(2,'-'),(2,'-'),(2,'-'),(2,'-')])) # No values remaining
        self.assertEqual(None,one_sparse([(2,'+'),(2,'+'),(4,'+'),(4,'+')])) # Bitsum sum of sign is inccorect