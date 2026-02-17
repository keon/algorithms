[![PyPI version](https://badge.fury.io/py/algorithms.svg)](https://badge.fury.io/py/algorithms)
[![Open Source Helpers](https://www.codetriage.com/keon/algorithms/badges/users.svg)](https://www.codetriage.com/keon/algorithms)

<p align="center"><img src="https://raw.githubusercontent.com/keon/algorithms/master/docs/source/_static/logo/logotype1blue.png"></p>

# Pythonic Data Structures and Algorithms

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
| Linked List | `linked_list.py` | `SinglyLinkedListNode`, `DoublyLinkedListNode` |
| Priority Queue | `priority_queue.py` | `PriorityQueue` |
| Queue | `queue.py` | `ArrayQueue`, `LinkedListQueue` |
| Red-Black Tree | `red_black_tree.py` | `RBTree` |
| Segment Tree | `segment_tree.py`, `iterative_segment_tree.py` | `SegmentTree` |
| Separate Chaining Hash Table | `separate_chaining_hash_table.py` | `SeparateChainingHashTable` |
| Stack | `stack.py` | `ArrayStack`, `LinkedListStack` |
| Trie | `trie.py` | `Trie` |
| Union-Find | `union_find.py` | `Union` |

## Algorithms

### Array

- [delete_nth](algorithms/array/delete_nth.py)
- [flatten](algorithms/array/flatten.py)
- [garage](algorithms/array/garage.py)
- [josephus](algorithms/array/josephus.py)
- [limit](algorithms/array/limit.py)
- [longest_non_repeat](algorithms/array/longest_non_repeat.py)
- [max_ones_index](algorithms/array/max_ones_index.py)
- [merge_intervals](algorithms/array/merge_intervals.py)
- [missing_ranges](algorithms/array/missing_ranges.py)
- [move_zeros](algorithms/array/move_zeros.py)
- [n_sum](algorithms/array/n_sum.py)
- [plus_one](algorithms/array/plus_one.py)
- [remove_duplicates](algorithms/array/remove_duplicates.py)
- [rotate](algorithms/array/rotate.py)
- [summarize_ranges](algorithms/array/summarize_ranges.py)
- [three_sum](algorithms/array/three_sum.py)
- [top_1](algorithms/array/top_1.py)
- [trimmean](algorithms/array/trimmean.py)
- [two_sum](algorithms/array/two_sum.py)

### Backtracking

- [add_operators](algorithms/backtracking/add_operators.py)
- [anagram](algorithms/backtracking/anagram.py)
- [array_sum_combinations](algorithms/backtracking/array_sum_combinations.py)
- [combination_sum](algorithms/backtracking/combination_sum.py)
- [factor_combinations](algorithms/backtracking/factor_combinations.py)
- [find_words](algorithms/backtracking/find_words.py)
- [generate_abbreviations](algorithms/backtracking/generate_abbreviations.py)
- [generate_parenthesis](algorithms/backtracking/generate_parenthesis.py)
- [letter_combination](algorithms/backtracking/letter_combination.py)
- [palindrome_partitioning](algorithms/backtracking/palindrome_partitioning.py)
- [pattern_match](algorithms/backtracking/pattern_match.py)
- [permute](algorithms/backtracking/permute.py)
- [permute_unique](algorithms/backtracking/permute_unique.py)
- [subsets](algorithms/backtracking/subsets.py)
- [subsets_unique](algorithms/backtracking/subsets_unique.py)

### Bit Manipulation

- [add_bitwise_operator](algorithms/bit_manipulation/add_bitwise_operator.py)
- [binary_gap](algorithms/bit_manipulation/binary_gap.py)
- [bit_operation](algorithms/bit_manipulation/bit_operation.py)
- [bytes_int_conversion](algorithms/bit_manipulation/bytes_int_conversion.py)
- [count_flips_to_convert](algorithms/bit_manipulation/count_flips_to_convert.py)
- [count_ones](algorithms/bit_manipulation/count_ones.py)
- [find_difference](algorithms/bit_manipulation/find_difference.py)
- [find_missing_number](algorithms/bit_manipulation/find_missing_number.py)
- [flip_bit_longest_sequence](algorithms/bit_manipulation/flip_bit_longest_sequence.py)
- [has_alternative_bit](algorithms/bit_manipulation/has_alternative_bit.py)
- [insert_bit](algorithms/bit_manipulation/insert_bit.py)
- [power_of_two](algorithms/bit_manipulation/power_of_two.py)
- [remove_bit](algorithms/bit_manipulation/remove_bit.py)
- [reverse_bits](algorithms/bit_manipulation/reverse_bits.py)
- [single_number](algorithms/bit_manipulation/single_number.py)
- [single_number2](algorithms/bit_manipulation/single_number2.py)
- [single_number3](algorithms/bit_manipulation/single_number3.py)
- [subsets](algorithms/bit_manipulation/subsets.py)
- [swap_pair](algorithms/bit_manipulation/swap_pair.py)

### Compression

- [elias](algorithms/compression/elias.py)
- [huffman_coding](algorithms/compression/huffman_coding.py)
- [rle_compression](algorithms/compression/rle_compression.py)

### Dynamic Programming

- [buy_sell_stock](algorithms/dynamic_programming/buy_sell_stock.py)
- [climbing_stairs](algorithms/dynamic_programming/climbing_stairs.py)
- [coin_change](algorithms/dynamic_programming/coin_change.py)
- [combination_sum](algorithms/dynamic_programming/combination_sum.py)
- [edit_distance](algorithms/dynamic_programming/edit_distance.py)
- [egg_drop](algorithms/dynamic_programming/egg_drop.py)
- [fibonacci](algorithms/dynamic_programming/fib.py)
- [hosoya_triangle](algorithms/dynamic_programming/hosoya_triangle.py)
- [house_robber](algorithms/dynamic_programming/house_robber.py)
- [int_divide](algorithms/dynamic_programming/int_divide.py)
- [job_scheduling](algorithms/dynamic_programming/job_scheduling.py)
- [k_factor](algorithms/dynamic_programming/k_factor.py)
- [knapsack](algorithms/dynamic_programming/knapsack.py)
- [longest_common_subsequence](algorithms/dynamic_programming/longest_common_subsequence.py)
- [longest_increasing](algorithms/dynamic_programming/longest_increasing.py)
- [matrix_chain_order](algorithms/dynamic_programming/matrix_chain_order.py)
- [max_product_subarray](algorithms/dynamic_programming/max_product_subarray.py)
- [max_subarray](algorithms/dynamic_programming/max_subarray.py)
- [min_cost_path](algorithms/dynamic_programming/min_cost_path.py)
- [num_decodings](algorithms/dynamic_programming/num_decodings.py)
- [planting_trees](algorithms/dynamic_programming/planting_trees.py)
- [regex_matching](algorithms/dynamic_programming/regex_matching.py)
- [rod_cut](algorithms/dynamic_programming/rod_cut.py)
- [word_break](algorithms/dynamic_programming/word_break.py)

### Graph

- [a_star](algorithms/graph/a_star.py)
- [all_factors](algorithms/graph/all_factors.py)
- [all_pairs_shortest_path](algorithms/graph/all_pairs_shortest_path.py)
- [bellman_ford](algorithms/graph/bellman_ford.py)
- [check_bipartite](algorithms/graph/check_bipartite.py)
- [check_digraph_strongly_connected](algorithms/graph/check_digraph_strongly_connected.py)
- [clone_graph](algorithms/graph/clone_graph.py)
- [count_connected_number_of_component](algorithms/graph/count_connected_number_of_component.py)
- [count_islands (BFS)](algorithms/graph/count_islands_bfs.py)
- [count_islands (DFS)](algorithms/graph/count_islands_dfs.py)
- [count_islands (Union-Find)](algorithms/graph/count_islands_unionfind.py)
- [cycle_detection](algorithms/graph/cycle_detection.py)
- [dijkstra](algorithms/graph/dijkstra.py)
- [find_all_cliques](algorithms/graph/find_all_cliques.py)
- [find_path](algorithms/graph/find_path.py)
- [kahns_algorithm](algorithms/graph/kahns_algorithm.py)
- [markov_chain](algorithms/graph/markov_chain.py)
- [maximum_flow](algorithms/graph/maximum_flow.py)
- [maximum_flow (BFS)](algorithms/graph/maximum_flow_bfs.py)
- [maximum_flow (DFS)](algorithms/graph/maximum_flow_dfs.py)
- [maze_search (BFS)](algorithms/graph/maze_search_bfs.py)
- [maze_search (DFS)](algorithms/graph/maze_search_dfs.py)
- [minimum_spanning_tree](algorithms/graph/minimum_spanning_tree.py)
- [pacific_atlantic](algorithms/graph/pacific_atlantic.py)
- [path_between_two_vertices_in_digraph](algorithms/graph/path_between_two_vertices_in_digraph.py)
- [prims_minimum_spanning](algorithms/graph/prims_minimum_spanning.py)
- [satisfiability](algorithms/graph/satisfiability.py)
- [shortest_distance_from_all_buildings](algorithms/graph/shortest_distance_from_all_buildings.py)
- [strongly_connected_components (Kosaraju)](algorithms/graph/strongly_connected_components_kosaraju.py)
- [sudoku_solver](algorithms/graph/sudoku_solver.py)
- [tarjan](algorithms/graph/tarjan.py)
- [topological_sort (BFS)](algorithms/graph/topological_sort_bfs.py)
- [topological_sort (DFS)](algorithms/graph/topological_sort_dfs.py)
- [transitive_closure (DFS)](algorithms/graph/transitive_closure_dfs.py)
- [traversal](algorithms/graph/traversal.py)
- [walls_and_gates](algorithms/graph/walls_and_gates.py)
- [word_ladder](algorithms/graph/word_ladder.py)

### Greedy

- [gale_shapley](algorithms/greedy/gale_shapley.py)
- [max_contiguous_subsequence_sum](algorithms/greedy/max_contiguous_subsequence_sum.py)

### Heap

- [k_closest_points](algorithms/heap/k_closest_points.py)
- [merge_sorted_k_lists](algorithms/heap/merge_sorted_k_lists.py)
- [skyline](algorithms/heap/skyline.py)
- [sliding_window_max](algorithms/heap/sliding_window_max.py)

### Linked List

- [add_two_numbers](algorithms/linked_list/add_two_numbers.py)
- [copy_random_pointer](algorithms/linked_list/copy_random_pointer.py)
- [delete_node](algorithms/linked_list/delete_node.py)
- [first_cyclic_node](algorithms/linked_list/first_cyclic_node.py)
- [intersection](algorithms/linked_list/intersection.py)
- [is_cyclic](algorithms/linked_list/is_cyclic.py)
- [is_palindrome](algorithms/linked_list/is_palindrome.py)
- [is_sorted](algorithms/linked_list/is_sorted.py)
- [kth_to_last](algorithms/linked_list/kth_to_last.py)
- [merge_two_list](algorithms/linked_list/merge_two_list.py)
- [partition](algorithms/linked_list/partition.py)
- [remove_duplicates](algorithms/linked_list/remove_duplicates.py)
- [remove_range](algorithms/linked_list/remove_range.py)
- [reverse](algorithms/linked_list/reverse.py)
- [rotate_list](algorithms/linked_list/rotate_list.py)
- [swap_in_pairs](algorithms/linked_list/swap_in_pairs.py)

### Map

- [is_anagram](algorithms/map/is_anagram.py)
- [is_isomorphic](algorithms/map/is_isomorphic.py)
- [longest_common_subsequence](algorithms/map/longest_common_subsequence.py)
- [longest_palindromic_subsequence](algorithms/map/longest_palindromic_subsequence.py)
- [randomized_set](algorithms/map/randomized_set.py)
- [valid_sudoku](algorithms/map/valid_sudoku.py)
- [word_pattern](algorithms/map/word_pattern.py)

### Math

- [base_conversion](algorithms/math/base_conversion.py)
- [chinese_remainder_theorem](algorithms/math/chinese_remainder_theorem.py)
- [combination](algorithms/math/combination.py)
- [cosine_similarity](algorithms/math/cosine_similarity.py)
- [decimal_to_binary_ip](algorithms/math/decimal_to_binary_ip.py)
- [diffie_hellman_key_exchange](algorithms/math/diffie_hellman_key_exchange.py)
- [distance_between_two_points](algorithms/math/distance_between_two_points.py)
- [euler_totient](algorithms/math/euler_totient.py)
- [extended_gcd](algorithms/math/extended_gcd.py)
- [factorial](algorithms/math/factorial.py)
- [fft](algorithms/math/fft.py)
- [find_order_simple](algorithms/math/find_order_simple.py)
- [find_primitive_root_simple](algorithms/math/find_primitive_root_simple.py)
- [gcd](algorithms/math/gcd.py)
- [generate_strobogrammtic](algorithms/math/generate_strobogrammtic.py)
- [hailstone](algorithms/math/hailstone.py)
- [is_strobogrammatic](algorithms/math/is_strobogrammatic.py)
- [krishnamurthy_number](algorithms/math/krishnamurthy_number.py)
- [magic_number](algorithms/math/magic_number.py)
- [modular_exponential](algorithms/math/modular_exponential.py)
- [modular_inverse](algorithms/math/modular_inverse.py)
- [next_bigger](algorithms/math/next_bigger.py)
- [next_perfect_square](algorithms/math/next_perfect_square.py)
- [nth_digit](algorithms/math/nth_digit.py)
- [num_digits](algorithms/math/num_digits.py)
- [num_perfect_squares](algorithms/math/num_perfect_squares.py)
- [polynomial](algorithms/math/polynomial.py)
- [power](algorithms/math/power.py)
- [prime_check](algorithms/math/prime_check.py)
- [primes_sieve_of_eratosthenes](algorithms/math/primes_sieve_of_eratosthenes.py)
- [pythagoras](algorithms/math/pythagoras.py)
- [rabin_miller](algorithms/math/rabin_miller.py)
- [recursive_binomial_coefficient](algorithms/math/recursive_binomial_coefficient.py)
- [rsa](algorithms/math/rsa.py)
- [sqrt_precision_factor](algorithms/math/sqrt_precision_factor.py)
- [summing_digits](algorithms/math/summing_digits.py)
- [surface_area_of_torus](algorithms/math/surface_area_of_torus.py)
- [symmetry_group_cycle_index](algorithms/math/symmetry_group_cycle_index.py)

### Matrix

- [bomb_enemy](algorithms/matrix/bomb_enemy.py)
- [cholesky_matrix_decomposition](algorithms/matrix/cholesky_matrix_decomposition.py)
- [copy_transform](algorithms/matrix/copy_transform.py)
- [count_paths](algorithms/matrix/count_paths.py)
- [crout_matrix_decomposition](algorithms/matrix/crout_matrix_decomposition.py)
- [matrix_exponentiation](algorithms/matrix/matrix_exponentiation.py)
- [matrix_inversion](algorithms/matrix/matrix_inversion.py)
- [multiply](algorithms/matrix/multiply.py)
- [rotate_image](algorithms/matrix/rotate_image.py)
- [search_in_sorted_matrix](algorithms/matrix/search_in_sorted_matrix.py)
- [sort_matrix_diagonally](algorithms/matrix/sort_matrix_diagonally.py)
- [sparse_dot_vector](algorithms/matrix/sparse_dot_vector.py)
- [sparse_mul](algorithms/matrix/sparse_mul.py)
- [spiral_traversal](algorithms/matrix/spiral_traversal.py)
- [sudoku_validator](algorithms/matrix/sudoku_validator.py)
- [sum_sub_squares](algorithms/matrix/sum_sub_squares.py)

### Queue

- [max_sliding_window](algorithms/queue/max_sliding_window.py)
- [moving_average](algorithms/queue/moving_average.py)
- [reconstruct_queue](algorithms/queue/reconstruct_queue.py)
- [zigzagiterator](algorithms/queue/zigzagiterator.py)

### Searching

- [binary_search](algorithms/searching/binary_search.py)
- [find_min_rotate](algorithms/searching/find_min_rotate.py)
- [first_occurrence](algorithms/searching/first_occurrence.py)
- [generalized_binary_search](algorithms/searching/generalized_binary_search.py)
- [interpolation_search](algorithms/searching/interpolation_search.py)
- [jump_search](algorithms/searching/jump_search.py)
- [last_occurrence](algorithms/searching/last_occurrence.py)
- [linear_search](algorithms/searching/linear_search.py)
- [next_greatest_letter](algorithms/searching/next_greatest_letter.py)
- [search_insert](algorithms/searching/search_insert.py)
- [search_range](algorithms/searching/search_range.py)
- [search_rotate](algorithms/searching/search_rotate.py)
- [ternary_search](algorithms/searching/ternary_search.py)
- [two_sum](algorithms/searching/two_sum.py)

### Set

- [find_keyboard_row](algorithms/set/find_keyboard_row.py)
- [randomized_set](algorithms/set/randomized_set.py)
- [set_covering](algorithms/set/set_covering.py)

### Sorting

- [bead_sort](algorithms/sorting/bead_sort.py)
- [bitonic_sort](algorithms/sorting/bitonic_sort.py)
- [bogo_sort](algorithms/sorting/bogo_sort.py)
- [bubble_sort](algorithms/sorting/bubble_sort.py)
- [bucket_sort](algorithms/sorting/bucket_sort.py)
- [cocktail_shaker_sort](algorithms/sorting/cocktail_shaker_sort.py)
- [comb_sort](algorithms/sorting/comb_sort.py)
- [counting_sort](algorithms/sorting/counting_sort.py)
- [cycle_sort](algorithms/sorting/cycle_sort.py)
- [exchange_sort](algorithms/sorting/exchange_sort.py)
- [gnome_sort](algorithms/sorting/gnome_sort.py)
- [heap_sort](algorithms/sorting/heap_sort.py)
- [insertion_sort](algorithms/sorting/insertion_sort.py)
- [meeting_rooms](algorithms/sorting/meeting_rooms.py)
- [merge_sort](algorithms/sorting/merge_sort.py)
- [pancake_sort](algorithms/sorting/pancake_sort.py)
- [pigeonhole_sort](algorithms/sorting/pigeonhole_sort.py)
- [quick_sort](algorithms/sorting/quick_sort.py)
- [radix_sort](algorithms/sorting/radix_sort.py)
- [selection_sort](algorithms/sorting/selection_sort.py)
- [shell_sort](algorithms/sorting/shell_sort.py)
- [sort_colors](algorithms/sorting/sort_colors.py)
- [stooge_sort](algorithms/sorting/stooge_sort.py)
- [wiggle_sort](algorithms/sorting/wiggle_sort.py)

### Stack

- [is_consecutive](algorithms/stack/is_consecutive.py)
- [is_sorted](algorithms/stack/is_sorted.py)
- [longest_abs_path](algorithms/stack/longest_abs_path.py)
- [ordered_stack](algorithms/stack/ordered_stack.py)
- [remove_min](algorithms/stack/remove_min.py)
- [simplify_path](algorithms/stack/simplify_path.py)
- [stutter](algorithms/stack/stutter.py)
- [switch_pairs](algorithms/stack/switch_pairs.py)
- [valid_parenthesis](algorithms/stack/valid_parenthesis.py)

### Streaming

- [misra_gries](algorithms/streaming/misra_gries.py)
- [one_sparse_recovery](algorithms/streaming/one_sparse_recovery.py)

### String

- [add_binary](algorithms/string/add_binary.py)
- [atbash_cipher](algorithms/string/atbash_cipher.py)
- [breaking_bad](algorithms/string/breaking_bad.py)
- [caesar_cipher](algorithms/string/caesar_cipher.py)
- [check_pangram](algorithms/string/check_pangram.py)
- [contain_string](algorithms/string/contain_string.py)
- [count_binary_substring](algorithms/string/count_binary_substring.py)
- [decode_string](algorithms/string/decode_string.py)
- [delete_reoccurring](algorithms/string/delete_reoccurring.py)
- [domain_extractor](algorithms/string/domain_extractor.py)
- [encode_decode](algorithms/string/encode_decode.py)
- [first_unique_char](algorithms/string/first_unique_char.py)
- [fizzbuzz](algorithms/string/fizzbuzz.py)
- [group_anagrams](algorithms/string/group_anagrams.py)
- [int_to_roman](algorithms/string/int_to_roman.py)
- [is_palindrome](algorithms/string/is_palindrome.py)
- [is_rotated](algorithms/string/is_rotated.py)
- [judge_circle](algorithms/string/judge_circle.py)
- [knuth_morris_pratt](algorithms/string/knuth_morris_pratt.py)
- [license_number](algorithms/string/license_number.py)
- [longest_common_prefix](algorithms/string/longest_common_prefix.py)
- [longest_palindromic_substring](algorithms/string/longest_palindromic_substring.py)
- [make_sentence](algorithms/string/make_sentence.py)
- [merge_string_checker](algorithms/string/merge_string_checker.py)
- [min_distance](algorithms/string/min_distance.py)
- [multiply_strings](algorithms/string/multiply_strings.py)
- [one_edit_distance](algorithms/string/one_edit_distance.py)
- [panagram](algorithms/string/panagram.py)
- [rabin_karp](algorithms/string/rabin_karp.py)
- [repeat_string](algorithms/string/repeat_string.py)
- [repeat_substring](algorithms/string/repeat_substring.py)
- [reverse_string](algorithms/string/reverse_string.py)
- [reverse_vowel](algorithms/string/reverse_vowel.py)
- [reverse_words](algorithms/string/reverse_words.py)
- [roman_to_int](algorithms/string/roman_to_int.py)
- [rotate](algorithms/string/rotate.py)
- [strip_url_params](algorithms/string/strip_url_params.py)
- [strong_password](algorithms/string/strong_password.py)
- [text_justification](algorithms/string/text_justification.py)
- [unique_morse](algorithms/string/unique_morse.py)
- [validate_coordinates](algorithms/string/validate_coordinates.py)
- [word_squares](algorithms/string/word_squares.py)

### Tree

- [bin_tree_to_list](algorithms/tree/bin_tree_to_list.py)
- [binary_tree_paths](algorithms/tree/binary_tree_paths.py)
- [bst_array_to_bst](algorithms/tree/bst_array_to_bst.py)
- [bst_closest_value](algorithms/tree/bst_closest_value.py)
- [bst_count_left_node](algorithms/tree/bst_count_left_node.py)
- [bst_delete_node](algorithms/tree/bst_delete_node.py)
- [bst_depth_sum](algorithms/tree/bst_depth_sum.py)
- [bst_height](algorithms/tree/bst_height.py)
- [bst_is_bst](algorithms/tree/bst_is_bst.py)
- [bst_iterator](algorithms/tree/bst_iterator.py)
- [bst_kth_smallest](algorithms/tree/bst_kth_smallest.py)
- [bst_lowest_common_ancestor](algorithms/tree/bst_lowest_common_ancestor.py)
- [bst_num_empty](algorithms/tree/bst_num_empty.py)
- [bst_predecessor](algorithms/tree/bst_predecessor.py)
- [bst_serialize_deserialize](algorithms/tree/bst_serialize_deserialize.py)
- [bst_successor](algorithms/tree/bst_successor.py)
- [bst_unique_bst](algorithms/tree/bst_unique_bst.py)
- [bst_validate_bst](algorithms/tree/bst_validate_bst.py)
- [construct_tree_postorder_preorder](algorithms/tree/construct_tree_postorder_preorder.py)
- [deepest_left](algorithms/tree/deepest_left.py)
- [invert_tree](algorithms/tree/invert_tree.py)
- [is_balanced](algorithms/tree/is_balanced.py)
- [is_subtree](algorithms/tree/is_subtree.py)
- [is_symmetric](algorithms/tree/is_symmetric.py)
- [longest_consecutive](algorithms/tree/longest_consecutive.py)
- [lowest_common_ancestor](algorithms/tree/lowest_common_ancestor.py)
- [max_height](algorithms/tree/max_height.py)
- [max_path_sum](algorithms/tree/max_path_sum.py)
- [min_height](algorithms/tree/min_height.py)
- [path_sum](algorithms/tree/path_sum.py)
- [path_sum2](algorithms/tree/path_sum2.py)
- [pretty_print](algorithms/tree/pretty_print.py)
- [same_tree](algorithms/tree/same_tree.py)
- [traversal_inorder](algorithms/tree/traversal_inorder.py)
- [traversal_level_order](algorithms/tree/traversal_level_order.py)
- [traversal_postorder](algorithms/tree/traversal_postorder.py)
- [traversal_preorder](algorithms/tree/traversal_preorder.py)
- [traversal_zigzag](algorithms/tree/traversal_zigzag.py)
- [trie_add_and_search](algorithms/tree/trie_add_and_search.py)

## Contributing

Thanks for your interest in contributing! There are many ways to get involved. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Maintainers

- [Keon Kim](https://github.com/keon)

## Contributors

Thanks to [all the contributors](https://github.com/keon/algorithms/graphs/contributors) who helped build this repo.

## License

[MIT](LICENSE)
