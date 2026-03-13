"""Tests for data structures in algorithms/data_structures."""

import unittest

from algorithms.data_structures.avl_tree import AvlTree
from algorithms.data_structures.hash_table import HashTable, ResizableHashTable
from algorithms.data_structures.red_black_tree import RBNode, RBTree
from algorithms.data_structures.segment_tree import SegmentTree
from algorithms.data_structures.separate_chaining_hash_table import (
    SeparateChainingHashTable,
)
from algorithms.data_structures.trie import Trie
from algorithms.data_structures.union_find import Union


class TestRBTree(unittest.TestCase):
    def _make_tree(self, values):
        tree = RBTree()
        for v in values:
            tree.insert(RBNode(v, 1))
        return tree

    def test_insert_single(self):
        tree = self._make_tree([5])
        result = tree.inorder()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["val"], 5)

    def test_insert_multiple_sorted(self):
        values = [11, 2, 14, 1, 7, 15, 5, 8, 4]
        tree = self._make_tree(values)
        result = tree.inorder()
        vals = [r["val"] for r in result]
        self.assertEqual(vals, sorted(values))

    def test_root_is_black(self):
        tree = self._make_tree([10, 5, 15])
        self.assertEqual(tree.root.color, 0)

    def test_empty_tree(self):
        tree = RBTree()
        self.assertIsNone(tree.root)
        self.assertEqual(tree.inorder(), [])

    def test_insert_duplicates_order(self):
        tree = self._make_tree([3, 1, 2])
        result = tree.inorder()
        vals = [r["val"] for r in result]
        self.assertEqual(vals, [1, 2, 3])


class TestAvlTree(unittest.TestCase):
    def test_insert_single(self):
        tree = AvlTree()
        tree.insert(10)
        self.assertIsNotNone(tree.node)
        self.assertEqual(tree.node.val, 10)

    def test_insert_multiple_root_exists(self):
        tree = AvlTree()
        for v in [5, 3, 7, 1, 4]:
            tree.insert(v)
        self.assertIsNotNone(tree.node)

    def test_balanced_after_insert(self):
        tree = AvlTree()
        for v in [1, 2, 3, 4, 5]:
            tree.insert(v)
        # Tree should remain balanced; height should be <= log2(5)+1 ~ 3
        self.assertLessEqual(tree.height, 3)

    def test_empty_tree(self):
        tree = AvlTree()
        self.assertIsNone(tree.node)
        self.assertEqual(tree.in_order_traverse(), [])

    def test_in_order_traverse_populated(self):
        tree = AvlTree()
        for v in [5, 3, 7, 1, 4]:
            tree.insert(v)
        self.assertEqual(tree.in_order_traverse(), [1, 3, 4, 5, 7])

    def test_insert_balance_factor(self):
        tree = AvlTree()
        for v in [5, 4, 3, 2, 1]:
            tree.insert(v)
        # After balancing, the balance factor should be within [-1, 1]
        self.assertIn(tree.balance, [-1, 0, 1])


class TestTrie(unittest.TestCase):
    def test_insert_and_search(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))

    def test_search_missing(self):
        trie = Trie()
        trie.insert("apple")
        self.assertFalse(trie.search("app"))

    def test_starts_with(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.starts_with("app"))
        self.assertFalse(trie.starts_with("apl"))

    def test_empty_trie(self):
        trie = Trie()
        self.assertFalse(trie.search("anything"))
        self.assertFalse(trie.starts_with("a"))

    def test_multiple_words(self):
        trie = Trie()
        for w in ["cat", "car", "card", "care"]:
            trie.insert(w)
        self.assertTrue(trie.search("card"))
        self.assertFalse(trie.search("ca"))
        self.assertTrue(trie.starts_with("ca"))

    def test_insert_single_char(self):
        trie = Trie()
        trie.insert("a")
        self.assertTrue(trie.search("a"))
        self.assertFalse(trie.search("b"))


class TestUnionFind(unittest.TestCase):
    def test_add_and_root(self):
        uf = Union()
        uf.add(1)
        self.assertEqual(uf.root(1), 1)

    def test_unite_connects(self):
        uf = Union()
        uf.add(1)
        uf.add(2)
        uf.unite(1, 2)
        self.assertEqual(uf.root(1), uf.root(2))

    def test_not_connected(self):
        uf = Union()
        uf.add(1)
        uf.add(2)
        self.assertNotEqual(uf.root(1), uf.root(2))

    def test_count_decrements_on_unite(self):
        uf = Union()
        uf.add(1)
        uf.add(2)
        uf.add(3)
        self.assertEqual(uf.count, 3)
        uf.unite(1, 2)
        self.assertEqual(uf.count, 2)

    def test_unite_same_element(self):
        uf = Union()
        uf.add(1)
        uf.unite(1, 1)
        self.assertEqual(uf.count, 1)

    def test_transitive_connectivity(self):
        uf = Union()
        for x in [1, 2, 3]:
            uf.add(x)
        uf.unite(1, 2)
        uf.unite(2, 3)
        self.assertEqual(uf.root(1), uf.root(3))


class TestSegmentTree(unittest.TestCase):
    def test_max_query(self):
        tree = SegmentTree([2, 4, 5, 3, 4], max)
        self.assertEqual(tree.query(2, 4), 5)

    def test_sum_query(self):
        tree = SegmentTree([1, 2, 3, 4, 5], lambda a, b: a + b)
        self.assertEqual(tree.query(0, 4), 15)

    def test_single_element_query(self):
        tree = SegmentTree([7, 2, 9], max)
        self.assertEqual(tree.query(0, 0), 7)
        self.assertEqual(tree.query(2, 2), 9)

    def test_full_range_max(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        tree = SegmentTree(arr, max)
        self.assertEqual(tree.query(0, len(arr) - 1), 9)


class TestHashTable(unittest.TestCase):
    def test_put_and_get(self):
        ht = HashTable()
        ht.put(1, "one")
        self.assertEqual(ht.get(1), "one")

    def test_get_missing(self):
        ht = HashTable()
        self.assertIsNone(ht.get(99))

    def test_delete(self):
        ht = HashTable()
        ht.put(1, "one")
        ht.del_(1)
        self.assertIsNone(ht.get(1))

    def test_update_existing(self):
        ht = HashTable()
        ht.put(1, "one")
        ht.put(1, "ONE")
        self.assertEqual(ht.get(1), "ONE")

    def test_len(self):
        ht = HashTable()
        ht.put(1, "a")
        ht.put(2, "b")
        self.assertEqual(len(ht), 2)

    def test_bracket_operators(self):
        ht = HashTable()
        ht[5] = "five"
        self.assertEqual(ht[5], "five")
        del ht[5]
        self.assertIsNone(ht[5])


class TestResizableHashTable(unittest.TestCase):
    def test_put_and_get(self):
        ht = ResizableHashTable()
        ht.put(1, "a")
        self.assertEqual(ht.get(1), "a")

    def test_resizes_automatically(self):
        ht = ResizableHashTable()
        for i in range(20):
            ht.put(i, str(i))
        for i in range(20):
            self.assertEqual(ht.get(i), str(i))


class TestSeparateChainingHashTable(unittest.TestCase):
    def test_put_and_get(self):
        table = SeparateChainingHashTable()
        table.put("hello", "world")
        self.assertEqual(table.get("hello"), "world")

    def test_get_missing(self):
        table = SeparateChainingHashTable()
        self.assertIsNone(table.get("missing"))

    def test_delete(self):
        table = SeparateChainingHashTable()
        table.put("key", "value")
        table.del_("key")
        self.assertIsNone(table.get("key"))

    def test_len(self):
        table = SeparateChainingHashTable()
        table.put("a", 1)
        table.put("b", 2)
        self.assertEqual(len(table), 2)

    def test_collision_handling(self):
        # Force collision by using small table
        table = SeparateChainingHashTable(size=1)
        table.put("x", 10)
        table.put("y", 20)
        self.assertEqual(table.get("x"), 10)
        self.assertEqual(table.get("y"), 20)

    def test_bracket_operators(self):
        table = SeparateChainingHashTable()
        table["k"] = "v"
        self.assertEqual(table["k"], "v")
        del table["k"]
        self.assertIsNone(table["k"])


if __name__ == "__main__":
    unittest.main()
