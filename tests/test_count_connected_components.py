#import modules
import unittest
from algorithms.graph import count_connected_number_of_component

class TestConnectedComponentInGraph(unittest.TestCase):
	""" Class to performs unit tests """
	
	def test_count_connected_components(self):
		"""
		   Test Function that test the different cases of count connected components
	        
		    0----------2    1--------5      3    
	            |
	            |
	            4
	            
	            output = 3

		"""
		expected_result = 3
		
		# adjacency list representation of graph
		l = [[2],
		    [5],
		    [0,4],
		    [],
		    [2],
		    [1]
		]

		size = 5
		result = count_connected_number_of_component.count_components(l,size)
		self.assertEqual(result,expected_result)

if __name__ == '__main__':

    unittest.main()
		
		
	       
