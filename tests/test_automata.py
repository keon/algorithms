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
    
        self.assertEqual(False, DFA(transitions, start, final, "000111100"))
        self.assertEqual(True, DFA(transitions, start, final, "111000011"))
        
        transitions1 = {
            '0': {'0': '1', '1': '0'},
            '1': {'0': '2', '1': '0'},
            '2': {'0': '2', '1': '3'},
            '3': {'0': '3', '1': '3'}
        }    
        
        final1 = ['0', '1', '2']
        start1 = '0'
        
        self.assertEqual(False, DFA(transitions1, start1, final1, "0001111"))
        self.assertEqual(True, DFA(transitions1, start1, final1, "01010101"))
        
        transitions2 = {
            '0': {'a': '0', 'b': '1'},
            '1': {'a': '0', 'b': '2'},
            '2': {'a': '3', 'b': '2'},
            '3': {'a': '3', 'b': '3'}
        }
        
        final2=['3']
        start2 = '0'

        self.assertEqual(False, DFA(transitions2, start2, final2, "aaabbb"))
        self.assertEqual(True, DFA(transitions2, start2, final2, "baabba"))
        
if __name__ == '__main__':
    unittest.main()
