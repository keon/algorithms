from algorithms.automata import DFA


import unittest


class TestDFA(unittest.TestCase):
    def test_DFA(self):
    
        transitions = {
            'a': {'1': 'a', '0': 'b'},
            'b': {'1': 'b', '0': 'a'}
        }

        final=['a']
        start = 'a'
    
        self.assertEqual(True, DFA(transitions, start, final, "000111100"))
        self.assertEqual(False, DFA(transitions, start, final, "111000011"))

if __name__ == '__main__':
    unittest.main()
