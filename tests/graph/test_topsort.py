from algorithms.sort import (
    top_sort, top_sort_recursive
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
        res = top_sort_recursive(self.depGraph)
        #print(res)
        self.assertTrue(res.index('g') < res.index('e'))
        res = top_sort(self.depGraph)
        self.assertTrue(res.index('g') < res.index('e'))

if __name__ == '__main__':
    unittest.main()
