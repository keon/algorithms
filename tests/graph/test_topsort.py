from algorithms.sort import (
    topological_sort, topological_sort_recursive
)

import unittest

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.depGraph = {
                            "a" : [ "b" ],
                            "b" : [ "c" ],
                            "c" :  [ 'e'],
                            'e' : [ 'g' ],
                            "d" : [ ],
                            "f" : ["e" , "d"],
                            "g" : [ ]
                        }
        
    def test_topsort(self):
        res = topological_sort_recursive(self.depGraph)
        #print(res)
        self.assertTrue(res.index('g') < res.index('e'))
        res = topological_sort_recursive(self.depGraph)
        self.assertTrue(res.index('g') < res.index('e'))

if __name__ == '__main__':
  unittest.main()
