"""
Given a list of system packages,
some packages cannot be installed until the other packages are installed.
Provide a valid sequence to install all of the packages.
e.g.
a relies on b
b relies on c
then a valid sequence is [c, b, a]
"""
import unittest


def topological_sort(G):

    def topological_sort_util(G, out, visited, start):
        if start in visited:
          return
        visited.add(start)
        for child in G[start]:
          topological_sort_util(G, out, visited, child)
        out.append(start)
    
    visited = set()
    out = []
    for pac in G:
      topological_sort_util(G, out, visited, pac)
    return out
  

class TestSuite(unittest.TestCase):
    
    def test_topological_sort(self):
        
        dependencies = {
                        "a" : ["b"],
                        "b" : ["c"],
                        "c" : ["e"],
                        'e' : [],
                        "d" : [],
                        "f" : ["e", "d"]
                        }
        self.assertListEqual(topological_sort(dependencies),
                             ['e', 'c', 'b', 'a', 'd', 'f'])


if __name__ == '__main__':
    
    unittest.main()
