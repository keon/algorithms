from algorithms.map import (
    HashTable, ResizableHashTable,
    Node, SeparateChainingHashTable,
    word_pattern,
    is_isomorphic,
    is_anagram
)

import unittest

class TestHashTable(unittest.TestCase):
    def test_one_entry(self):
        m = HashTable(10)
        m.put(1, '1')
        self.assertEqual('1', m.get(1))

    def test_add_entry_bigger_than_table_size(self):
        m = HashTable(10)
        m.put(11, '1')
        self.assertEqual('1', m.get(11))

    def test_get_none_if_key_missing_and_hash_collision(self):
        m = HashTable(10)
        m.put(1, '1')
        self.assertEqual(None, m.get(11))

    def test_two_entries_with_same_hash(self):
        m = HashTable(10)
        m.put(1, '1')
        m.put(11, '11')
        self.assertEqual('1', m.get(1))
        self.assertEqual('11', m.get(11))

    def test_get_on_full_table_does_halts(self):
        # and does not search forever
        m = HashTable(10)
        for i in range(10, 20):
            m.put(i, i)
        self.assertEqual(None, m.get(1))

    def test_delete_key(self):
        m = HashTable(10)
        for i in range(5):
            m.put(i, i**2)
        m.del_(1)
        self.assertEqual(None, m.get(1))
        self.assertEqual(4,m.get(2))

    def test_delete_key_and_reassign(self):
        m = HashTable(10)
        m.put(1, 1)
        del m[1]
        m.put(1, 2)
        self.assertEqual(2, m.get(1))

    def test_assigning_to_full_table_throws_error(self):
        m = HashTable(3)
        m.put(1, 1)
        m.put(2, 2)
        m.put(3, 3)
        with self.assertRaises(ValueError):
            m.put(4, 4)

    def test_len_trivial(self):
        m = HashTable(10)
        self.assertEqual(0, len(m))
        for i in range(10):
            m.put(i, i)
            self.assertEqual(i + 1, len(m))

    def test_len_after_deletions(self):
        m = HashTable(10)
        m.put(1, 1)
        self.assertEqual(1, len(m))
        m.del_(1)
        self.assertEqual(0, len(m))
        m.put(11, 42)
        self.assertEqual(1, len(m))

    def test_resizable_hash_table(self):
        m = ResizableHashTable()
        self.assertEqual(ResizableHashTable.MIN_SIZE, m.size)
        for i in range(ResizableHashTable.MIN_SIZE):
            m.put(i, 'foo')
        self.assertEqual(ResizableHashTable.MIN_SIZE * 2, m.size)
        self.assertEqual('foo', m.get(1))
        self.assertEqual('foo', m.get(3))
        self.assertEqual('foo', m.get(ResizableHashTable.MIN_SIZE - 1))

    def test_fill_up_the_limit(self):
        m = HashTable(10)
        for i in range(10):
            m.put(i,i**2)
        for i in range(10):
            self.assertEqual(i**2,m.get(i))


class TestSeparateChainingHashTable(unittest.TestCase):
    def test_one_entry(self):
        m = SeparateChainingHashTable(10)
        m.put(1, '1')
        self.assertEqual('1', m.get(1))

    def test_two_entries_with_same_hash(self):
        m = SeparateChainingHashTable(10)
        m.put(1, '1')
        m.put(11, '11')
        self.assertEqual('1', m.get(1))
        self.assertEqual('11', m.get(11))

    def test_len_trivial(self):
        m = SeparateChainingHashTable(10)
        self.assertEqual(0, len(m))
        for i in range(10):
            m.put(i, i)
            self.assertEqual(i + 1, len(m))

    def test_len_after_deletions(self):
        m = SeparateChainingHashTable(10)
        m.put(1, 1)
        self.assertEqual(1, len(m))
        m.del_(1)
        self.assertEqual(0, len(m))
        m.put(11, 42)
        self.assertEqual(1, len(m))

    def test_delete_key(self):
        m = SeparateChainingHashTable(10)
        for i in range(5):
            m.put(i, i**2)
        m.del_(1)
        self.assertEqual(None, m.get(1))
        self.assertEqual(4, m.get(2))

    def test_delete_key_and_reassign(self):
        m = SeparateChainingHashTable(10)
        m.put(1, 1)
        del m[1]
        m.put(1, 2)
        self.assertEqual(2, m.get(1))

    def test_add_entry_bigger_than_table_size(self):
        m = SeparateChainingHashTable(10)
        m.put(11, '1')
        self.assertEqual('1', m.get(11))

    def test_get_none_if_key_missing_and_hash_collision(self):
        m = SeparateChainingHashTable(10)
        m.put(1, '1')
        self.assertEqual(None, m.get(11))


class TestWordPattern(unittest.TestCase):
    def test_word_pattern(self):
        self.assertTrue(word_pattern("abba", "dog cat cat dog"))
        self.assertFalse(word_pattern("abba", "dog cat cat fish"))
        self.assertFalse(word_pattern("abba", "dog dog dog dog"))
        self.assertFalse(word_pattern("aaaa", "dog cat cat dog"))


class TestIsSomorphic(unittest.TestCase):
    def test_is_isomorphic(self):
        self.assertTrue(is_isomorphic("egg", "add"))
        self.assertFalse(is_isomorphic("foo", "bar"))
        self.assertTrue(is_isomorphic("paper", "title"))


class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram("anagram", "nagaram"))
        self.assertFalse(is_anagram("rat", "car"))




if __name__ == "__main__":
    unittest.main()
