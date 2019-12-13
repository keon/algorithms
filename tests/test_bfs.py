from algorithms.bfs import (
    maze_search,
    shortest_distance_from_all_buildings,
    ladder_length
)

import unittest


class TestMazeSearch(unittest.TestCase):
    
    def test_maze_search(self):
        grid_1 = [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]
        self.assertEqual(14, maze_search(grid_1))
        grid_2 = [[1,0,0],[0,1,1],[0,1,1]]
        self.assertEqual(-1, maze_search(grid_2))


class TestWordLadder(unittest.TestCase):

    def test_ladder_length(self):

        # hit -> hot -> dot -> dog -> cog
        self.assertEqual(5, ladder_length('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))

        # pick -> sick -> sink -> sank -> tank == 5
        self.assertEqual(5, ladder_length('pick', 'tank',
                                          ['tock', 'tick', 'sank', 'sink', 'sick']))

        # live -> life == 1, no matter what is the word_list.
        self.assertEqual(1, ladder_length('live', 'life', ['hoho', 'luck']))

        # 0 length from ate -> ate
        self.assertEqual(0, ladder_length('ate', 'ate', []))

        # not possible to reach !
        self.assertEqual(-1, ladder_length('rahul', 'coder', ['blahh', 'blhah']))


if __name__ == "__main__":
    unittest.main()
