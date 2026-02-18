[![PyPI version](https://badge.fury.io/py/algorithms.svg)](https://badge.fury.io/py/algorithms)
[![Open Source Helpers](https://www.codetriage.com/keon/algorithms/badges/users.svg)](https://www.codetriage.com/keon/algorithms)

# algorithms

Minimal, clean, and well-documented implementations of data structures and algorithms in Python 3.

Each file is self-contained with docstrings, type hints, and complexity notes &mdash; designed to be read and learned from.

## Quick Start

### Install

```bash
pip install algorithms
```

### Use

```python
from algorithms.sorting import merge_sort

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# [3, 9, 10, 27, 38, 43, 82]
```

```python
from algorithms.data_structures import BinaryHeap, Trie, BST
from algorithms.graph import dijkstra, bellman_ford
from algorithms.tree import TreeNode
```

### Examples

**Graph &mdash; Dijkstra's shortest path:**

```python
from algorithms.graph import dijkstra

graph = {
    "s": {"a": 2, "b": 1},
    "a": {"s": 3, "b": 4, "c": 8},
    "b": {"s": 4, "a": 2, "d": 2},
    "c": {"a": 2, "d": 7, "t": 4},
    "d": {"b": 1, "c": 11, "t": 5},
    "t": {"c": 3, "d": 5},
}
print(dijkstra(graph, "s", "t"))
# (8, ['s', 'b', 'd', 't'])
```

**Dynamic programming &mdash; coin change:**

```python
from algorithms.dynamic_programming import coin_change

# Minimum coins to make amount 29 using denominations [1, 5, 10, 25]
print(coin_change([1, 5, 10, 25], 29))
# 7   (25 + 1 + 1 + 1 + 1)
```

**Backtracking &mdash; generate permutations:**

```python
from algorithms.backtracking import permute

print(permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

**Data structures &mdash; binary heap:**

```python
from algorithms.data_structures import BinaryHeap

heap = BinaryHeap()
for val in [5, 3, 8, 1, 9]:
    heap.insert(val)
print(heap.remove_min())  # 1
print(heap.remove_min())  # 3
```

**Searching &mdash; binary search:**

```python
from algorithms.searching import binary_search

print(binary_search([1, 3, 5, 7, 9, 11], 7))
# 3   (index of target)
```

**Tree &mdash; inorder traversal:**

```python
from algorithms.tree import TreeNode
from algorithms.tree import inorder

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(inorder(root))
# [1, 2, 3, 4, 6]
```

**String &mdash; Knuth-Morris-Pratt pattern matching:**

```python
from algorithms.string import knuth_morris_pratt

print(knuth_morris_pratt("abxabcabcaby", "abcaby"))
# 6   (starting index of match)
```

### Run Tests

```bash
python -m pytest tests/
```

## Project Structure

```
algorithms/
    data_structures/     # Reusable data structure implementations
    array/               # Array manipulation algorithms
    backtracking/        # Constraint satisfaction & enumeration
    bit_manipulation/    # Bitwise operations & tricks
    compression/         # Encoding & compression schemes
    dynamic_programming/ # Optimal substructure & memoization
    graph/               # Graph algorithms (BFS, DFS, shortest path, flow, ...)
    greedy/              # Greedy strategies
    heap/                # Heap-based algorithms
    linked_list/         # Linked list algorithms
    map/                 # Hash-map-based algorithms
    math/                # Number theory, combinatorics, algebra
    matrix/              # 2D array & linear algebra operations
    queue/               # Queue-based algorithms
    searching/           # Search algorithms (binary, linear, ...)
    set/                 # Set-based algorithms
    sorting/             # Sorting algorithms
    stack/               # Stack-based algorithms
    streaming/           # Streaming & sketching algorithms
    string/              # String matching, manipulation, parsing
    tree/                # Tree algorithms (traversal, BST ops, ...)
tests/                   # One test file per topic
```

## Data Structures

All core data structures live in [`algorithms/data_structures/`](algorithms/data_structures):

| Data Structure | Module | Key Classes |
|---|---|---|
| AVL Tree | `avl_tree.py` | `AvlTree` |
| B-Tree | `b_tree.py` | `BTree` |
| Binary Search Tree | `bst.py` | `BST` |
| Fenwick Tree | `fenwick_tree.py` | `Fenwick_Tree` |
| Graph | `graph.py` | `Node`, `DirectedEdge`, `DirectedGraph` |
| Hash Table | `hash_table.py` | `HashTable`, `ResizableHashTable` |
| Heap | `heap.py` | `BinaryHeap` |
| KD Tree | `kd_tree.py` | `KDTree` |
| Linked List | `linked_list.py` | `SinglyLinkedListNode`, `DoublyLinkedListNode` |
| Priority Queue | `priority_queue.py` | `PriorityQueue` |
| Queue | `queue.py` | `ArrayQueue`, `LinkedListQueue` |
| Red-Black Tree | `red_black_tree.py` | `RBTree` |
| Segment Tree | `segment_tree.py`, `iterative_segment_tree.py` | `SegmentTree` |
| Separate Chaining Hash Table | `separate_chaining_hash_table.py` | `SeparateChainingHashTable` |
| Sqrt Decomposition | `sqrt_decomposition.py` | `SqrtDecomposition` |
| Stack | `stack.py` | `ArrayStack`, `LinkedListStack` |
| Trie | `trie.py` | `Trie` |
| Union-Find | `union_find.py` | `Union` |

## Algorithms

### Array

- [delete_nth](algorithms/array/delete_nth.py) &mdash; keep at most N occurrences of each element
- [flatten](algorithms/array/flatten.py) &mdash; recursively flatten nested arrays into a single list
- [garage](algorithms/array/garage.py) &mdash; minimum swaps to rearrange a parking lot
- [josephus](algorithms/array/josephus.py) &mdash; eliminate every k-th person in a circular arrangement
- [limit](algorithms/array/limit.py) &mdash; filter elements within min/max bounds
- [longest_non_repeat](algorithms/array/longest_non_repeat.py) &mdash; longest substring without repeating characters
- [max_ones_index](algorithms/array/max_ones_index.py) &mdash; find the zero to flip for the longest run of ones
- [merge_intervals](algorithms/array/merge_intervals.py) &mdash; combine overlapping intervals
- [missing_ranges](algorithms/array/missing_ranges.py) &mdash; find gaps between a low and high bound
- [move_zeros](algorithms/array/move_zeros.py) &mdash; move all zeros to the end, preserving order
- [n_sum](algorithms/array/n_sum.py) &mdash; find all unique n-tuples that sum to a target
- [plus_one](algorithms/array/plus_one.py) &mdash; add one to a number represented as a digit array
- [remove_duplicates](algorithms/array/remove_duplicates.py) &mdash; remove duplicate elements preserving order
- [rotate](algorithms/array/rotate.py) &mdash; rotate an array right by k positions
- [summarize_ranges](algorithms/array/summarize_ranges.py) &mdash; summarize consecutive integers as range tuples
- [three_sum](algorithms/array/three_sum.py) &mdash; find all unique triplets that sum to zero
- [top_1](algorithms/array/top_1.py) &mdash; find the most frequently occurring values
- [trimmean](algorithms/array/trimmean.py) &mdash; compute mean after trimming extreme values
- [two_sum](algorithms/array/two_sum.py) &mdash; find two indices whose values sum to a target

### Backtracking

- [add_operators](algorithms/backtracking/add_operators.py) &mdash; insert +, -, * between digits to reach a target
- [anagram](algorithms/backtracking/anagram.py) &mdash; check if two strings are anagrams
- [array_sum_combinations](algorithms/backtracking/array_sum_combinations.py) &mdash; find three-element combos from arrays that hit a target sum
- [combination_sum](algorithms/backtracking/combination_sum.py) &mdash; find combinations (with reuse) that sum to a target
- [factor_combinations](algorithms/backtracking/factor_combinations.py) &mdash; generate all factor combinations of a number
- [find_words](algorithms/backtracking/find_words.py) &mdash; find words on a letter board via trie-based search
- [generate_abbreviations](algorithms/backtracking/generate_abbreviations.py) &mdash; generate all possible abbreviations of a word
- [generate_parenthesis](algorithms/backtracking/generate_parenthesis.py) &mdash; generate all valid parenthesis combinations
- [letter_combination](algorithms/backtracking/letter_combination.py) &mdash; phone keypad digit-to-letter combinations
- [palindrome_partitioning](algorithms/backtracking/palindrome_partitioning.py) &mdash; partition a string into palindromic substrings
- [pattern_match](algorithms/backtracking/pattern_match.py) &mdash; match a string to a pattern via bijection mapping
- [permute](algorithms/backtracking/permute.py) &mdash; generate all permutations of distinct elements
- [permute_unique](algorithms/backtracking/permute_unique.py) &mdash; generate unique permutations when duplicates exist
- [subsets](algorithms/backtracking/subsets.py) &mdash; generate all subsets (power set)
- [minimax](algorithms/backtracking/minimax.py) &mdash; game-tree search with alpha-beta pruning
- [subsets_unique](algorithms/backtracking/subsets_unique.py) &mdash; generate unique subsets when duplicates exist

### Bit Manipulation

- [add_bitwise_operator](algorithms/bit_manipulation/add_bitwise_operator.py) &mdash; add two integers using only bitwise operations
- [binary_gap](algorithms/bit_manipulation/binary_gap.py) &mdash; longest distance between consecutive 1-bits
- [bit_operation](algorithms/bit_manipulation/bit_operation.py) &mdash; get, set, clear, and update individual bits
- [bytes_int_conversion](algorithms/bit_manipulation/bytes_int_conversion.py) &mdash; convert between integers and byte sequences
- [count_flips_to_convert](algorithms/bit_manipulation/count_flips_to_convert.py) &mdash; count bit flips needed to convert one integer to another
- [count_ones](algorithms/bit_manipulation/count_ones.py) &mdash; count the number of 1-bits (Hamming weight)
- [find_difference](algorithms/bit_manipulation/find_difference.py) &mdash; find the added character between two strings using XOR
- [find_missing_number](algorithms/bit_manipulation/find_missing_number.py) &mdash; find a missing number in a sequence using XOR
- [flip_bit_longest_sequence](algorithms/bit_manipulation/flip_bit_longest_sequence.py) &mdash; longest run of 1s after flipping a single 0
- [gray_code](algorithms/bit_manipulation/gray_code.py) &mdash; generate Gray code sequences and convert between Gray and binary
- [has_alternative_bit](algorithms/bit_manipulation/has_alternative_bit.py) &mdash; check if binary representation has alternating bits
- [insert_bit](algorithms/bit_manipulation/insert_bit.py) &mdash; insert bits at a specific position in an integer
- [power_of_two](algorithms/bit_manipulation/power_of_two.py) &mdash; check if an integer is a power of two
- [remove_bit](algorithms/bit_manipulation/remove_bit.py) &mdash; remove a bit at a given position
- [reverse_bits](algorithms/bit_manipulation/reverse_bits.py) &mdash; reverse all 32 bits of an unsigned integer
- [single_number](algorithms/bit_manipulation/single_number.py) &mdash; find the element appearing once (others appear twice) via XOR
- [single_number2](algorithms/bit_manipulation/single_number2.py) &mdash; find the element appearing once (others appear three times)
- [single_number3](algorithms/bit_manipulation/single_number3.py) &mdash; find two unique elements (others appear twice)
- [subsets](algorithms/bit_manipulation/subsets.py) &mdash; generate all subsets using bitmask enumeration
- [swap_pair](algorithms/bit_manipulation/swap_pair.py) &mdash; swap adjacent bit pairs in an integer

### Compression

- [elias](algorithms/compression/elias.py) &mdash; Elias gamma and delta universal integer coding
- [huffman_coding](algorithms/compression/huffman_coding.py) &mdash; variable-length prefix codes for lossless compression
- [rle_compression](algorithms/compression/rle_compression.py) &mdash; run-length encoding for consecutive character compression

### Dynamic Programming

- [bitmask](algorithms/dynamic_programming/bitmask.py) &mdash; travelling salesman problem via bitmask dynamic programming
- [buy_sell_stock](algorithms/dynamic_programming/buy_sell_stock.py) &mdash; maximize profit from a stock price array
- [climbing_stairs](algorithms/dynamic_programming/climbing_stairs.py) &mdash; count ways to climb stairs taking 1 or 2 steps
- [coin_change](algorithms/dynamic_programming/coin_change.py) &mdash; minimum coins to make a given amount
- [combination_sum](algorithms/dynamic_programming/combination_sum.py) &mdash; count combinations that sum to a target (with reuse)
- [count_paths_dp](algorithms/dynamic_programming/count_paths_dp.py) &mdash; count paths in a grid using recursion, memoization, and bottom-up DP
- [edit_distance](algorithms/dynamic_programming/edit_distance.py) &mdash; minimum edits to transform one string into another
- [egg_drop](algorithms/dynamic_programming/egg_drop.py) &mdash; minimize trials to find the critical floor
- [fibonacci](algorithms/dynamic_programming/fib.py) &mdash; compute Fibonacci numbers with memoization
- [hosoya_triangle](algorithms/dynamic_programming/hosoya_triangle.py) &mdash; generate the Hosoya triangle of Fibonacci-like numbers
- [house_robber](algorithms/dynamic_programming/house_robber.py) &mdash; maximize loot from non-adjacent houses
- [int_divide](algorithms/dynamic_programming/int_divide.py) &mdash; count the number of integer partitions
- [job_scheduling](algorithms/dynamic_programming/job_scheduling.py) &mdash; maximize profit from weighted job scheduling
- [k_factor](algorithms/dynamic_programming/k_factor.py) &mdash; find the k-factor of a string pattern
- [knapsack](algorithms/dynamic_programming/knapsack.py) &mdash; maximize value under a weight constraint
- [longest_common_subsequence](algorithms/dynamic_programming/longest_common_subsequence.py) &mdash; find the longest common subsequence of two strings
- [longest_increasing](algorithms/dynamic_programming/longest_increasing.py) &mdash; find the longest increasing subsequence
- [matrix_chain_order](algorithms/dynamic_programming/matrix_chain_order.py) &mdash; minimize scalar multiplications for matrix chain
- [max_product_subarray](algorithms/dynamic_programming/max_product_subarray.py) &mdash; find the contiguous subarray with maximum product
- [max_subarray](algorithms/dynamic_programming/max_subarray.py) &mdash; maximum sum subarray (Kadane's algorithm)
- [min_cost_path](algorithms/dynamic_programming/min_cost_path.py) &mdash; minimum-cost path through a grid
- [num_decodings](algorithms/dynamic_programming/num_decodings.py) &mdash; count ways to decode a digit string into letters
- [planting_trees](algorithms/dynamic_programming/planting_trees.py) &mdash; optimize tree planting for maximum profit
- [regex_matching](algorithms/dynamic_programming/regex_matching.py) &mdash; match a string against a pattern with `.` and `*` wildcards
- [rod_cut](algorithms/dynamic_programming/rod_cut.py) &mdash; maximize revenue from cutting a rod into pieces
- [word_break](algorithms/dynamic_programming/word_break.py) &mdash; check if a string can be segmented into dictionary words

### Graph

- [a_star](algorithms/graph/a_star.py) &mdash; heuristic shortest-path search (A* algorithm)
- [all_factors](algorithms/graph/all_factors.py) &mdash; find all factor combinations of a number
- [all_pairs_shortest_path](algorithms/graph/all_pairs_shortest_path.py) &mdash; Floyd-Warshall all-pairs shortest paths
- [bellman_ford](algorithms/graph/bellman_ford.py) &mdash; single-source shortest path with negative edge weights
- [blossom](algorithms/graph/blossom.py) &mdash; Edmonds' blossom algorithm for maximum matching in general graphs
- [check_bipartite](algorithms/graph/check_bipartite.py) &mdash; determine if a graph is two-colorable
- [check_digraph_strongly_connected](algorithms/graph/check_digraph_strongly_connected.py) &mdash; check if a directed graph is strongly connected
- [clone_graph](algorithms/graph/clone_graph.py) &mdash; deep-copy an undirected graph
- [count_connected_number_of_component](algorithms/graph/count_connected_number_of_component.py) &mdash; count connected components in an undirected graph
- [count_islands (BFS)](algorithms/graph/count_islands_bfs.py) &mdash; count islands in a grid using breadth-first search
- [count_islands (DFS)](algorithms/graph/count_islands_dfs.py) &mdash; count islands in a grid using depth-first search
- [count_islands (Union-Find)](algorithms/graph/count_islands_unionfind.py) &mdash; count islands using a disjoint-set structure
- [cycle_detection](algorithms/graph/cycle_detection.py) &mdash; detect cycles in a directed graph
- [dijkstra](algorithms/graph/dijkstra.py) &mdash; single-source shortest path for non-negative weights
- [dijkstra_heapq](algorithms/graph/dijkstra_heapq.py) &mdash; heap-optimised Dijkstra in O((V+E) log V) for sparse graphs
- [find_all_cliques](algorithms/graph/find_all_cliques.py) &mdash; Bron-Kerbosch algorithm for finding all cliques
- [find_path](algorithms/graph/find_path.py) &mdash; find paths between two vertices
- [kahns_algorithm](algorithms/graph/kahns_algorithm.py) &mdash; topological sort via in-degree counting (Kahn's)
- [markov_chain](algorithms/graph/markov_chain.py) &mdash; Markov chain probability modeling
- [maximum_flow](algorithms/graph/maximum_flow.py) &mdash; compute maximum flow in a flow network
- [maximum_flow (BFS)](algorithms/graph/maximum_flow_bfs.py) &mdash; Edmonds-Karp max-flow (BFS-based Ford-Fulkerson)
- [maximum_flow (DFS)](algorithms/graph/maximum_flow_dfs.py) &mdash; Ford-Fulkerson max-flow via DFS augmenting paths
- [maze_search (BFS)](algorithms/graph/maze_search_bfs.py) &mdash; find shortest path through a maze using BFS
- [maze_search (DFS)](algorithms/graph/maze_search_dfs.py) &mdash; find a path through a maze using DFS
- [minimum_spanning_tree](algorithms/graph/minimum_spanning_tree.py) &mdash; Kruskal's minimum spanning tree
- [pacific_atlantic](algorithms/graph/pacific_atlantic.py) &mdash; find cells that can flow to both oceans
- [path_between_two_vertices_in_digraph](algorithms/graph/path_between_two_vertices_in_digraph.py) &mdash; check if a path exists in a directed graph
- [prims_minimum_spanning](algorithms/graph/prims_minimum_spanning.py) &mdash; Prim's minimum spanning tree
- [satisfiability](algorithms/graph/satisfiability.py) &mdash; 2-SAT satisfiability via implication graph
- [shortest_distance_from_all_buildings](algorithms/graph/shortest_distance_from_all_buildings.py) &mdash; find the optimal meeting point in a grid
- [strongly_connected_components (Kosaraju)](algorithms/graph/strongly_connected_components_kosaraju.py) &mdash; Kosaraju's SCC algorithm
- [sudoku_solver](algorithms/graph/sudoku_solver.py) &mdash; solve a Sudoku puzzle using constraint backtracking
- [tarjan](algorithms/graph/tarjan.py) &mdash; Tarjan's strongly connected components algorithm
- [topological_sort (BFS)](algorithms/graph/topological_sort_bfs.py) &mdash; topological ordering using BFS (Kahn's variant)
- [topological_sort (DFS)](algorithms/graph/topological_sort_dfs.py) &mdash; topological ordering using DFS post-order
- [transitive_closure (DFS)](algorithms/graph/transitive_closure_dfs.py) &mdash; compute the transitive closure of a graph
- [traversal](algorithms/graph/traversal.py) &mdash; BFS and DFS graph traversal
- [walls_and_gates](algorithms/graph/walls_and_gates.py) &mdash; fill each empty room with distance to nearest gate
- [word_ladder](algorithms/graph/word_ladder.py) &mdash; shortest word-to-word transformation sequence

### Greedy

- [gale_shapley](algorithms/greedy/gale_shapley.py) &mdash; stable matching for bipartite preferences (Gale-Shapley)
- [max_contiguous_subsequence_sum](algorithms/greedy/max_contiguous_subsequence_sum.py) &mdash; maximum contiguous subarray sum (Kadane's algorithm)

### Heap

- [k_closest_points](algorithms/heap/k_closest_points.py) &mdash; find k points closest to the origin
- [merge_sorted_k_lists](algorithms/heap/merge_sorted_k_lists.py) &mdash; merge k sorted linked lists using a min-heap
- [skyline](algorithms/heap/skyline.py) &mdash; compute the skyline silhouette from building rectangles
- [sliding_window_max](algorithms/heap/sliding_window_max.py) &mdash; maximum value in each sliding window position

### Linked List

- [add_two_numbers](algorithms/linked_list/add_two_numbers.py) &mdash; add two numbers stored as reversed linked lists
- [copy_random_pointer](algorithms/linked_list/copy_random_pointer.py) &mdash; deep-copy a linked list with random pointers
- [delete_node](algorithms/linked_list/delete_node.py) &mdash; delete a node given only a reference to it
- [first_cyclic_node](algorithms/linked_list/first_cyclic_node.py) &mdash; find the first node where a cycle begins (Floyd's)
- [intersection](algorithms/linked_list/intersection.py) &mdash; find the intersection point of two singly linked lists
- [is_cyclic](algorithms/linked_list/is_cyclic.py) &mdash; detect whether a linked list has a cycle
- [is_palindrome](algorithms/linked_list/is_palindrome.py) &mdash; check if a linked list reads the same forwards and backwards
- [is_sorted](algorithms/linked_list/is_sorted.py) &mdash; check if a linked list is sorted in order
- [kth_to_last](algorithms/linked_list/kth_to_last.py) &mdash; find the k-th element from the end
- [merge_two_list](algorithms/linked_list/merge_two_list.py) &mdash; merge two sorted linked lists into one
- [partition](algorithms/linked_list/partition.py) &mdash; partition a list around a pivot value
- [remove_duplicates](algorithms/linked_list/remove_duplicates.py) &mdash; remove duplicate values from a linked list
- [remove_range](algorithms/linked_list/remove_range.py) &mdash; remove nodes within a given index range
- [reverse](algorithms/linked_list/reverse.py) &mdash; reverse a linked list iteratively and recursively
- [rotate_list](algorithms/linked_list/rotate_list.py) &mdash; rotate a list right by k positions
- [swap_in_pairs](algorithms/linked_list/swap_in_pairs.py) &mdash; swap every two adjacent nodes

### Map

- [is_anagram](algorithms/map/is_anagram.py) &mdash; check if two strings are anagrams via character counting
- [is_isomorphic](algorithms/map/is_isomorphic.py) &mdash; check if two strings have the same character mapping structure
- [longest_common_subsequence](algorithms/map/longest_common_subsequence.py) &mdash; longest common substring using a hash map
- [longest_palindromic_subsequence](algorithms/map/longest_palindromic_subsequence.py) &mdash; longest palindromic substring via hash map
- [randomized_set](algorithms/map/randomized_set.py) &mdash; O(1) insert, delete, and get-random data structure
- [valid_sudoku](algorithms/map/valid_sudoku.py) &mdash; validate a Sudoku board configuration
- [word_pattern](algorithms/map/word_pattern.py) &mdash; check if a string follows a given pattern mapping

### Math

- [base_conversion](algorithms/math/base_conversion.py) &mdash; convert integers between arbitrary number bases
- [chinese_remainder_theorem](algorithms/math/chinese_remainder_theorem.py) &mdash; solve a system of modular congruences
- [combination](algorithms/math/combination.py) &mdash; compute binomial coefficients (n choose r)
- [cosine_similarity](algorithms/math/cosine_similarity.py) &mdash; compute cosine similarity between two vectors
- [decimal_to_binary_ip](algorithms/math/decimal_to_binary_ip.py) &mdash; convert an IP address between decimal and binary
- [diffie_hellman_key_exchange](algorithms/math/diffie_hellman_key_exchange.py) &mdash; Diffie-Hellman cryptographic key exchange
- [distance_between_two_points](algorithms/math/distance_between_two_points.py) &mdash; Euclidean distance in 2D space
- [euler_totient](algorithms/math/euler_totient.py) &mdash; count integers up to n that are coprime to n
- [extended_gcd](algorithms/math/extended_gcd.py) &mdash; extended Euclidean algorithm (GCD with coefficients)
- [factorial](algorithms/math/factorial.py) &mdash; compute n! iteratively and recursively
- [fft](algorithms/math/fft.py) &mdash; Fast Fourier Transform (Cooley-Tukey)
- [find_order_simple](algorithms/math/find_order_simple.py) &mdash; find the multiplicative order of an element mod n
- [find_primitive_root_simple](algorithms/math/find_primitive_root_simple.py) &mdash; find a primitive root modulo a prime
- [gcd](algorithms/math/gcd.py) &mdash; greatest common divisor and least common multiple
- [generate_strobogrammtic](algorithms/math/generate_strobogrammtic.py) &mdash; generate strobogrammatic numbers of length n
- [goldbach](algorithms/math/goldbach.py) &mdash; decompose an even number into a sum of two primes (Goldbach's conjecture)
- [hailstone](algorithms/math/hailstone.py) &mdash; Collatz conjecture (hailstone) sequence
- [is_strobogrammatic](algorithms/math/is_strobogrammatic.py) &mdash; check if a number looks the same upside-down
- [krishnamurthy_number](algorithms/math/krishnamurthy_number.py) &mdash; check if a number equals the sum of the factorials of its digits
- [linear_regression](algorithms/math/linear_regression.py) &mdash; ordinary least-squares linear regression with R² and RMSE
- [magic_number](algorithms/math/magic_number.py) &mdash; check if a number is a magic number
- [manhattan_distance](algorithms/math/manhattan_distance.py) &mdash; compute Manhattan (L1) distance between two points in any dimension
- [modular_exponential](algorithms/math/modular_exponential.py) &mdash; compute (base^exp) mod m efficiently
- [modular_inverse](algorithms/math/modular_inverse.py) &mdash; compute the modular multiplicative inverse
- [next_bigger](algorithms/math/next_bigger.py) &mdash; next larger number with the same digits
- [next_perfect_square](algorithms/math/next_perfect_square.py) &mdash; find the next perfect square after n
- [nth_digit](algorithms/math/nth_digit.py) &mdash; find the n-th digit in the sequence 1, 2, 3, ...
- [num_digits](algorithms/math/num_digits.py) &mdash; count the number of digits in an integer
- [num_perfect_squares](algorithms/math/num_perfect_squares.py) &mdash; minimum perfect squares that sum to n
- [polynomial](algorithms/math/polynomial.py) &mdash; polynomial and monomial arithmetic operations
- [polynomial_division](algorithms/math/polynomial_division.py) &mdash; polynomial long division returning quotient and remainder
- [power](algorithms/math/power.py) &mdash; compute x^n via binary exponentiation
- [prime_check](algorithms/math/prime_check.py) &mdash; check if a number is prime
- [primes_sieve_of_eratosthenes](algorithms/math/primes_sieve_of_eratosthenes.py) &mdash; generate primes up to n using the Sieve of Eratosthenes
- [pythagoras](algorithms/math/pythagoras.py) &mdash; Pythagorean theorem calculations
- [rabin_miller](algorithms/math/rabin_miller.py) &mdash; Miller-Rabin probabilistic primality test
- [recursive_binomial_coefficient](algorithms/math/recursive_binomial_coefficient.py) &mdash; binomial coefficient via Pascal's triangle recursion
- [rsa](algorithms/math/rsa.py) &mdash; RSA public-key encryption and decryption
- [sqrt_precision_factor](algorithms/math/sqrt_precision_factor.py) &mdash; square root to arbitrary precision (Newton's method)
- [summing_digits](algorithms/math/summing_digits.py) &mdash; recursively sum the digits of a number
- [surface_area_of_torus](algorithms/math/surface_area_of_torus.py) &mdash; calculate the surface area of a torus
- [symmetry_group_cycle_index](algorithms/math/symmetry_group_cycle_index.py) &mdash; cycle index polynomials for symmetry groups

### Matrix

- [bomb_enemy](algorithms/matrix/bomb_enemy.py) &mdash; maximize enemies killed by a single bomb placement
- [cholesky_matrix_decomposition](algorithms/matrix/cholesky_matrix_decomposition.py) &mdash; Cholesky decomposition of a positive-definite matrix
- [copy_transform](algorithms/matrix/copy_transform.py) &mdash; copy and transform a matrix
- [count_paths](algorithms/matrix/count_paths.py) &mdash; count paths from top-left to bottom-right of a grid
- [crout_matrix_decomposition](algorithms/matrix/crout_matrix_decomposition.py) &mdash; Crout's LU matrix decomposition
- [matrix_exponentiation](algorithms/matrix/matrix_exponentiation.py) &mdash; raise a matrix to the n-th power efficiently
- [matrix_inversion](algorithms/matrix/matrix_inversion.py) &mdash; compute the inverse of a square matrix
- [multiply](algorithms/matrix/multiply.py) &mdash; standard and Strassen matrix multiplication
- [rotate_image](algorithms/matrix/rotate_image.py) &mdash; rotate an n x n matrix 90 degrees in-place
- [search_in_sorted_matrix](algorithms/matrix/search_in_sorted_matrix.py) &mdash; search in a row- and column-sorted matrix
- [sort_matrix_diagonally](algorithms/matrix/sort_matrix_diagonally.py) &mdash; sort each diagonal of a matrix independently
- [sparse_dot_vector](algorithms/matrix/sparse_dot_vector.py) &mdash; dot product of two sparse vectors
- [sparse_mul](algorithms/matrix/sparse_mul.py) &mdash; multiply two sparse matrices efficiently
- [spiral_traversal](algorithms/matrix/spiral_traversal.py) &mdash; traverse a matrix in spiral order
- [sudoku_validator](algorithms/matrix/sudoku_validator.py) &mdash; validate that a Sudoku board follows all rules
- [sum_sub_squares](algorithms/matrix/sum_sub_squares.py) &mdash; sum of all k x k sub-squares in a matrix

### Queue

- [max_sliding_window](algorithms/queue/max_sliding_window.py) &mdash; maximum in each sliding window using a deque
- [moving_average](algorithms/queue/moving_average.py) &mdash; compute a running moving average from a stream
- [reconstruct_queue](algorithms/queue/reconstruct_queue.py) &mdash; reconstruct a queue from (height, count) pairs
- [zigzagiterator](algorithms/queue/zigzagiterator.py) &mdash; alternate elements from multiple iterators

### Searching

- [binary_search](algorithms/searching/binary_search.py) &mdash; search a sorted array in O(log n)
- [exponential_search](algorithms/searching/exponential_search.py) &mdash; search a sorted array by doubling the range then binary searching
- [find_min_rotate](algorithms/searching/find_min_rotate.py) &mdash; find the minimum in a rotated sorted array
- [first_occurrence](algorithms/searching/first_occurrence.py) &mdash; find the first occurrence of a target value
- [generalized_binary_search](algorithms/searching/generalized_binary_search.py) &mdash; binary search with a custom predicate
- [interpolation_search](algorithms/searching/interpolation_search.py) &mdash; search using value-based interpolation
- [jump_search](algorithms/searching/jump_search.py) &mdash; search a sorted array by jumping in fixed blocks
- [last_occurrence](algorithms/searching/last_occurrence.py) &mdash; find the last occurrence of a target value
- [linear_search](algorithms/searching/linear_search.py) &mdash; sequential scan through an unsorted array
- [next_greatest_letter](algorithms/searching/next_greatest_letter.py) &mdash; find the smallest letter greater than a target
- [search_insert](algorithms/searching/search_insert.py) &mdash; find the insertion position for a target value
- [search_range](algorithms/searching/search_range.py) &mdash; find the first and last positions of a target
- [search_rotate](algorithms/searching/search_rotate.py) &mdash; search in a rotated sorted array
- [sentinel_search](algorithms/searching/sentinel_search.py) &mdash; linear search optimized by placing a sentinel at the end
- [ternary_search](algorithms/searching/ternary_search.py) &mdash; search by dividing the array into three parts
- [two_sum](algorithms/searching/two_sum.py) &mdash; find two numbers that sum to a target

### Set

- [find_keyboard_row](algorithms/set/find_keyboard_row.py) &mdash; filter words that can be typed on one keyboard row
- [randomized_set](algorithms/set/randomized_set.py) &mdash; O(1) insert, delete, and random-element access
- [set_covering](algorithms/set/set_covering.py) &mdash; greedy approximation for the set cover problem

### Sorting

- [bead_sort](algorithms/sorting/bead_sort.py) &mdash; gravity-based natural sorting (bead/abacus sort)
- [bitonic_sort](algorithms/sorting/bitonic_sort.py) &mdash; parallel-friendly comparison sort via bitonic sequences
- [bogo_sort](algorithms/sorting/bogo_sort.py) &mdash; random permutation sort (intentionally inefficient)
- [bubble_sort](algorithms/sorting/bubble_sort.py) &mdash; repeatedly swap adjacent out-of-order elements
- [bucket_sort](algorithms/sorting/bucket_sort.py) &mdash; distribute elements into buckets, then sort each
- [cocktail_shaker_sort](algorithms/sorting/cocktail_shaker_sort.py) &mdash; bidirectional bubble sort
- [comb_sort](algorithms/sorting/comb_sort.py) &mdash; bubble sort improved with a shrinking gap
- [counting_sort](algorithms/sorting/counting_sort.py) &mdash; sort integers by counting occurrences
- [cycle_sort](algorithms/sorting/cycle_sort.py) &mdash; in-place sort that minimizes total writes
- [exchange_sort](algorithms/sorting/exchange_sort.py) &mdash; simple pairwise comparison and exchange
- [gnome_sort](algorithms/sorting/gnome_sort.py) &mdash; sort by swapping elements backward until ordered
- [heap_sort](algorithms/sorting/heap_sort.py) &mdash; sort via a binary heap (in-place, O(n log n))
- [insertion_sort](algorithms/sorting/insertion_sort.py) &mdash; build a sorted portion one element at a time
- [meeting_rooms](algorithms/sorting/meeting_rooms.py) &mdash; determine if meeting intervals overlap
- [merge_sort](algorithms/sorting/merge_sort.py) &mdash; divide-and-conquer stable sort (O(n log n))
- [pancake_sort](algorithms/sorting/pancake_sort.py) &mdash; sort using only prefix reversals
- [pigeonhole_sort](algorithms/sorting/pigeonhole_sort.py) &mdash; sort by placing elements into pigeonhole buckets
- [quick_sort](algorithms/sorting/quick_sort.py) &mdash; partition-based divide-and-conquer sort
- [radix_sort](algorithms/sorting/radix_sort.py) &mdash; non-comparative sort processing one digit at a time
- [selection_sort](algorithms/sorting/selection_sort.py) &mdash; repeatedly select the minimum and swap it forward
- [shell_sort](algorithms/sorting/shell_sort.py) &mdash; generalized insertion sort with a decreasing gap sequence
- [sort_colors](algorithms/sorting/sort_colors.py) &mdash; Dutch national flag three-way partition
- [stooge_sort](algorithms/sorting/stooge_sort.py) &mdash; recursive sort by dividing into overlapping thirds
- [wiggle_sort](algorithms/sorting/wiggle_sort.py) &mdash; rearrange into an alternating peak-valley pattern

### Stack

- [is_consecutive](algorithms/stack/is_consecutive.py) &mdash; check if stack elements are consecutive integers
- [is_sorted](algorithms/stack/is_sorted.py) &mdash; check if a stack is sorted in ascending order
- [longest_abs_path](algorithms/stack/longest_abs_path.py) &mdash; find the longest absolute file path in a file system string
- [ordered_stack](algorithms/stack/ordered_stack.py) &mdash; maintain a stack in sorted order
- [remove_min](algorithms/stack/remove_min.py) &mdash; remove the minimum element from a stack
- [simplify_path](algorithms/stack/simplify_path.py) &mdash; simplify a Unix-style file path
- [stutter](algorithms/stack/stutter.py) &mdash; duplicate each element in a stack
- [switch_pairs](algorithms/stack/switch_pairs.py) &mdash; swap adjacent pairs of stack elements
- [valid_parenthesis](algorithms/stack/valid_parenthesis.py) &mdash; check for balanced parentheses / brackets

### Streaming

- [misra_gries](algorithms/streaming/misra_gries.py) &mdash; approximate frequent-item detection in a data stream
- [one_sparse_recovery](algorithms/streaming/one_sparse_recovery.py) &mdash; recover a single non-zero element from a stream

### String

- [add_binary](algorithms/string/add_binary.py) &mdash; add two binary number strings
- [alphabet_board_path](algorithms/string/alphabet_board_path.py) &mdash; navigate a 5×5 alphabet board to spell a target word
- [atbash_cipher](algorithms/string/atbash_cipher.py) &mdash; Atbash substitution cipher (reverse the alphabet)
- [breaking_bad](algorithms/string/breaking_bad.py) &mdash; spell a string using periodic-table element symbols
- [caesar_cipher](algorithms/string/caesar_cipher.py) &mdash; Caesar shift cipher encryption / decryption
- [check_pangram](algorithms/string/check_pangram.py) &mdash; check if a string contains every letter of the alphabet
- [contain_string](algorithms/string/contain_string.py) &mdash; find a substring in a string (strStr)
- [count_binary_substring](algorithms/string/count_binary_substring.py) &mdash; count substrings with equal consecutive 0s and 1s
- [decode_string](algorithms/string/decode_string.py) &mdash; decode a run-length encoded string like `3[a2[c]]`
- [delete_reoccurring](algorithms/string/delete_reoccurring.py) &mdash; remove consecutive duplicate characters
- [domain_extractor](algorithms/string/domain_extractor.py) &mdash; extract a domain name from a URL
- [encode_decode](algorithms/string/encode_decode.py) &mdash; encode and decode a list of strings
- [first_unique_char](algorithms/string/first_unique_char.py) &mdash; find the first non-repeating character
- [fizzbuzz](algorithms/string/fizzbuzz.py) &mdash; classic FizzBuzz problem
- [group_anagrams](algorithms/string/group_anagrams.py) &mdash; group strings that are anagrams of each other
- [int_to_roman](algorithms/string/int_to_roman.py) &mdash; convert an integer to a Roman numeral string
- [is_palindrome](algorithms/string/is_palindrome.py) &mdash; check if a string reads the same forwards and backwards
- [is_rotated](algorithms/string/is_rotated.py) &mdash; check if one string is a rotation of another
- [judge_circle](algorithms/string/judge_circle.py) &mdash; determine if a sequence of moves returns to the origin
- [knuth_morris_pratt](algorithms/string/knuth_morris_pratt.py) &mdash; KMP linear-time pattern matching
- [license_number](algorithms/string/license_number.py) &mdash; reformat a license key string with dashes
- [longest_common_prefix](algorithms/string/longest_common_prefix.py) &mdash; find the longest common prefix among strings
- [longest_palindromic_substring](algorithms/string/longest_palindromic_substring.py) &mdash; find the longest palindromic substring
- [make_sentence](algorithms/string/make_sentence.py) &mdash; break a string into valid dictionary words
- [manacher](algorithms/string/manacher.py) &mdash; find the longest palindromic substring in O(n) time
- [merge_string_checker](algorithms/string/merge_string_checker.py) &mdash; check if a string is a valid merge of two others
- [min_distance](algorithms/string/min_distance.py) &mdash; minimum deletions to make two strings equal
- [multiply_strings](algorithms/string/multiply_strings.py) &mdash; multiply two numbers represented as strings
- [one_edit_distance](algorithms/string/one_edit_distance.py) &mdash; check if two strings are exactly one edit apart
- [panagram](algorithms/string/panagram.py) &mdash; find missing letters to complete a pangram
- [rabin_karp](algorithms/string/rabin_karp.py) &mdash; Rabin-Karp rolling-hash pattern matching
- [repeat_string](algorithms/string/repeat_string.py) &mdash; minimum string repeats to contain a substring
- [repeat_substring](algorithms/string/repeat_substring.py) &mdash; check if a string is built from a repeating pattern
- [reverse_string](algorithms/string/reverse_string.py) &mdash; reverse a string in-place
- [reverse_vowel](algorithms/string/reverse_vowel.py) &mdash; reverse only the vowels in a string
- [reverse_words](algorithms/string/reverse_words.py) &mdash; reverse the order of words in a string
- [roman_to_int](algorithms/string/roman_to_int.py) &mdash; convert a Roman numeral string to an integer
- [rotate](algorithms/string/rotate.py) &mdash; rotate a string by k positions
- [strip_url_params](algorithms/string/strip_url_params.py) &mdash; remove duplicate query parameters from a URL
- [swap_characters](algorithms/string/swap_characters.py) &mdash; check if one character swap can make two strings equal
- [strong_password](algorithms/string/strong_password.py) &mdash; check minimum changes needed for a strong password
- [text_justification](algorithms/string/text_justification.py) &mdash; justify text lines to a specified width
- [unique_morse](algorithms/string/unique_morse.py) &mdash; count unique Morse code representations of words
- [validate_coordinates](algorithms/string/validate_coordinates.py) &mdash; validate geographic latitude/longitude coordinates
- [word_squares](algorithms/string/word_squares.py) &mdash; find all valid word squares from a word list
- [z_algorithm](algorithms/string/z_algorithm.py) &mdash; Z-array computation for linear-time pattern matching

### Tree

- [bin_tree_to_list](algorithms/tree/bin_tree_to_list.py) &mdash; convert a binary tree to a doubly linked list
- [binary_tree_paths](algorithms/tree/binary_tree_paths.py) &mdash; enumerate all root-to-leaf paths
- [binary_tree_views](algorithms/tree/binary_tree_views.py) &mdash; left, right, top, and bottom views of a binary tree
- [bst_array_to_bst](algorithms/tree/bst_array_to_bst.py) &mdash; convert a sorted array into a height-balanced BST
- [bst_closest_value](algorithms/tree/bst_closest_value.py) &mdash; find the value closest to a target in a BST
- [bst_count_left_node](algorithms/tree/bst_count_left_node.py) &mdash; count the number of left-child nodes
- [bst_delete_node](algorithms/tree/bst_delete_node.py) &mdash; delete a node from a BST while preserving order
- [bst_depth_sum](algorithms/tree/bst_depth_sum.py) &mdash; sum of node values weighted by their depth
- [bst_height](algorithms/tree/bst_height.py) &mdash; calculate the height of a binary tree
- [bst_is_bst](algorithms/tree/bst_is_bst.py) &mdash; validate the binary search tree property
- [bst_iterator](algorithms/tree/bst_iterator.py) &mdash; lazy in-order iterator for a BST
- [bst_kth_smallest](algorithms/tree/bst_kth_smallest.py) &mdash; find the k-th smallest element in a BST
- [bst_lowest_common_ancestor](algorithms/tree/bst_lowest_common_ancestor.py) &mdash; lowest common ancestor exploiting BST ordering
- [bst_num_empty](algorithms/tree/bst_num_empty.py) &mdash; count empty (null) branches in a tree
- [bst_predecessor](algorithms/tree/bst_predecessor.py) &mdash; find the in-order predecessor of a BST node
- [bst_serialize_deserialize](algorithms/tree/bst_serialize_deserialize.py) &mdash; serialize a BST to a string and back
- [bst_successor](algorithms/tree/bst_successor.py) &mdash; find the in-order successor of a BST node
- [bst_unique_bst](algorithms/tree/bst_unique_bst.py) &mdash; count structurally unique BSTs for n keys (Catalan number)
- [bst_validate_bst](algorithms/tree/bst_validate_bst.py) &mdash; validate a BST using min/max range constraints
- [construct_tree_postorder_preorder](algorithms/tree/construct_tree_postorder_preorder.py) &mdash; reconstruct a tree from pre-order and post-order traversals
- [deepest_left](algorithms/tree/deepest_left.py) &mdash; find the deepest left leaf node
- [invert_tree](algorithms/tree/invert_tree.py) &mdash; mirror a binary tree (swap all left/right children)
- [is_balanced](algorithms/tree/is_balanced.py) &mdash; check if a tree is height-balanced
- [is_subtree](algorithms/tree/is_subtree.py) &mdash; check if one tree is a subtree of another
- [is_symmetric](algorithms/tree/is_symmetric.py) &mdash; check if a tree is a mirror of itself
- [longest_consecutive](algorithms/tree/longest_consecutive.py) &mdash; longest consecutive-value sequence in a tree
- [lowest_common_ancestor](algorithms/tree/lowest_common_ancestor.py) &mdash; find the lowest common ancestor of two nodes
- [max_height](algorithms/tree/max_height.py) &mdash; maximum depth (height) of a binary tree
- [max_path_sum](algorithms/tree/max_path_sum.py) &mdash; maximum sum along any path between two nodes
- [min_height](algorithms/tree/min_height.py) &mdash; minimum depth from root to the nearest leaf
- [path_sum](algorithms/tree/path_sum.py) &mdash; check if any root-to-leaf path sums to a target
- [path_sum2](algorithms/tree/path_sum2.py) &mdash; find all root-to-leaf paths that sum to a target
- [pretty_print](algorithms/tree/pretty_print.py) &mdash; pretty-print a binary tree to the console
- [same_tree](algorithms/tree/same_tree.py) &mdash; check if two binary trees are structurally identical
- [traversal_inorder](algorithms/tree/traversal_inorder.py) &mdash; in-order traversal (left, root, right)
- [traversal_level_order](algorithms/tree/traversal_level_order.py) &mdash; level-order (breadth-first) traversal
- [traversal_postorder](algorithms/tree/traversal_postorder.py) &mdash; post-order traversal (left, right, root)
- [traversal_preorder](algorithms/tree/traversal_preorder.py) &mdash; pre-order traversal (root, left, right)
- [traversal_zigzag](algorithms/tree/traversal_zigzag.py) &mdash; zigzag (alternating direction) level-order traversal
- [trie_add_and_search](algorithms/tree/trie_add_and_search.py) &mdash; trie with wildcard `.` search support

## Contributing

Thanks for your interest in contributing! There are many ways to get involved. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Maintainers

- [Keon Kim](https://github.com/keon)

## Contributors

Thanks to [all the contributors](https://github.com/keon/algorithms/graphs/contributors) who helped build this repo.

## License

[MIT](LICENSE)
