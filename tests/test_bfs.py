from algorithms.bfs import (
    maze_search,
    shortest_distance_from_all_buildings,
    word_ladder
)

import unittest

class TestMazeSearch(unittest.TestCase):
    
    def test_maze_search(self):
        grid = [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]
        self.assertEqual(14, maze_search(grid))
        
if __name__ == "__main__":
    unittest.main()
