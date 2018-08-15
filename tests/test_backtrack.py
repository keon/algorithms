from algorithms.backtrack import (
    add_operators,
    permute,
    permute_iter,
    anagram,
    array_sum_combinations,
    unique_array_sum_combinations,
    combination_sum,
    find_words,
    pattern_match,
)

import unittest
from algorithms.backtrack.generate_parenthesis import *


class TestAddOperator(unittest.TestCase):
    def test_add_operators(self):
        # "123", 6 -> ["1+2+3", "1*2*3"]
        s = "123"
        target = 6
        self.assertEqual(add_operators(s, target), ["1+2+3", "1*2*3"])
        # "232", 8 -> ["2*3+2", "2+3*2"]
        s = "232"
        target = 8
        self.assertEqual(add_operators(s, target), ["2+3*2", "2*3+2"])

        s = "123045"
        target = 3
        answer = ['1+2+3*0*4*5',
                  '1+2+3*0*45',
                  '1+2-3*0*4*5',
                  '1+2-3*0*45',
                  '1-2+3+0-4+5',
                  '1-2+3-0-4+5',
                  '1*2+3*0-4+5',
                  '1*2-3*0-4+5',
                  '1*23+0-4*5',
                  '1*23-0-4*5',
                  '12+3*0-4-5',
                  '12-3*0-4-5']
        self.assertEqual(add_operators(s, target), answer)


class TestPermuteAndAnagram(unittest.TestCase):

    def test_permute(self):
        perms = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        self.assertEqual(perms, permute("abc"))

    def test_permute_iter(self):
        it = permute_iter("abc")
        perms = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        for i in range(len(perms)):
            self.assertEqual(perms[i], next(it))

    def test_angram(self):
        self.assertTrue(anagram('apple', 'pleap'))
        self.assertFalse(anagram("apple", "cherry"))


class TestArrayCombinationSum(unittest.TestCase):

    def test_array_sum_combinations(self):
        A = [1, 2, 3, 3]
        B = [2, 3, 3, 4]
        C = [2, 3, 3, 4]
        target = 7
        answer = [[1, 2, 4], [1, 3, 3], [1, 3, 3], [1, 3, 3],
                  [1, 3, 3], [1, 4, 2], [2, 2, 3], [2, 2, 3],
                  [2, 3, 2], [2, 3, 2], [3, 2, 2], [3, 2, 2]]
        answer.sort()
        self.assertListEqual(sorted(array_sum_combinations(A, B, C, target)), answer)

    def test_unique_array_sum_combinations(self):
        A = [1, 2, 3, 3]
        B = [2, 3, 3, 4]
        C = [2, 3, 3, 4]
        target = 7
        answer = [(2, 3, 2), (3, 2, 2), (1, 2, 4),
                  (1, 4, 2), (2, 2, 3), (1, 3, 3)]
        answer.sort()
        self.assertListEqual(sorted(unique_array_sum_combinations(A, B, C, target)), answer)


class TestCombinationSum(unittest.TestCase):

    def check_sum(self, nums, target):
        if sum(nums) == target:
            return (True, nums)
        else:
            return (False, nums)

    def test_combination_sum(self):
        candidates1 = [2, 3, 6, 7]
        target1 = 7
        answer1 = [
            [2, 2, 3],
            [7]
        ]
        self.assertEqual(combination_sum(candidates1, target1), answer1)

        candidates2 = [2, 3, 5]
        target2 = 8
        answer2 = [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ]
        self.assertEqual(combination_sum(candidates2, target2), answer2)


class TestFindWords(unittest.TestCase):

    def test_normal(self):
        board = [
             ['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']
        ]

        words = ["oath", "pea", "eat", "rain"]
        self.assertEqual(find_words(board, words).sort(),
                         ['oath', 'eat'].sort())

    def test_none(self):
        board = [
             ['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']
        ]

        words = ["chicken", "nugget", "hello", "world"]
        self.assertEqual(find_words(board, words), [])

    def test_empty(self):
        board = []
        words = []
        self.assertEqual(find_words(board, words), [])

    def test_uneven(self):
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e']
        ]
        words = ["oath", "pea", "eat", "rain"]
        self.assertEqual(find_words(board, words), ['eat'])

    def test_repeat(self):
        board = [
            ['a', 'a', 'a'],
            ['a', 'a', 'a'],
            ['a', 'a', 'a']
        ]
        words = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        self.assertTrue(len(find_words(board, words)) == 5)


class TestPatternMatch(unittest.TestCase):

    def test_pattern_match(self):
        pattern1 = "abab"
        string1 = "redblueredblue"
        pattern2 = "aaaa"
        string2 = "asdasdasdasd"
        pattern3 = "aabb"
        string3 = "xyzabcxzyabc"

        self.assertTrue(pattern_match(pattern1, string1))
        self.assertTrue(pattern_match(pattern2, string2))
        self.assertFalse(pattern_match(pattern3, string3))

class TestGenerateParenthesis(unittest.TestCase):

    def test_generate_parenthesis(self):
        self.assertEqual(generate_parenthesis_v1(2), ['()()', '(())'])
        self.assertEqual(generate_parenthesis_v1(3), ['()()()', '()(())', '(())()', '(()())', '((()))'])
        self.assertEqual(generate_parenthesis_v2(2), ['(())', '()()'])
        self.assertEqual(generate_parenthesis_v2(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])

if __name__ == '__main__':

    unittest.main()

