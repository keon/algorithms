from algorithms.bfs import (
    maze_search,
    shortest_distance_from_all_buildings,
    word_ladder
)

import unittest

class TestMazeSearch(unittest.TestCase):
    
    def test_maze_search(self):
        grid_1 = [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]
        self.assertEqual(14, maze_search(grid_1))
        grid_2 = [[1,0,0],[0,1,1],[0,1,1]]
        self.assertEqual(-1, maze_search(grid_2))
        
if __name__ == "__main__":
    unittest.main()
