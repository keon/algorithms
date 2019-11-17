[![PyPI version](https://badge.fury.io/py/algorithms.svg)](https://badge.fury.io/py/algorithms)
[![Open Source Helpers](https://www.codetriage.com/keon/algorithms/badges/users.svg)](https://www.codetriage.com/keon/algorithms)
[![Build Status](https://travis-ci.org/keon/algorithms.svg?branch=master)](https://travis-ci.org/keon/algorithms)
[![Coverage Status](https://coveralls.io/repos/github/keon/algorithms/badge.svg?branch=master)](https://coveralls.io/github/keon/algorithms?branch=master)

<p align="center"><img src="https://raw.githubusercontent.com/keon/algorithms/master/docs/source/_static/logo/logotype1blue.png"></p>

Pythonic Data Structures and Algorithms
=========================================

Minimal and clean example implementations of data structures and algorithms in Python 3.

## Contributing
Thanks for your interest in contributing! There are many ways to contribute to this project. [Get started here](CONTRIBUTING.md)

## Tests

### Use unittest
For running all tests write down:

    $ python3 -m unittest discover tests

For running some specific tests you can do this as following (Ex: sort):

    $ python3 -m unittest tests.test_sort

### Use pytest
For running all tests write down:

    $ python3 -m pytest tests

## Install
If you want to use the API algorithms in your code, it is as simple as:

    $ pip3 install algorithms

You can test by creating a python file: (Ex: use `merge_sort` in `sort`)

```python3
from algorithms.sort import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort(my_list)
    print(my_list)
```

## Uninstall
If you want to uninstall algorithms, it is as simple as:

    $ pip3 uninstall -y algorithms

## List of Implementations

- [arrays](algorithms/arrays)
    - [delete_nth](algorithms/arrays/delete_nth.py)
    - [flatten](algorithms/arrays/flatten.py)
    - [garage](algorithms/arrays/garage.py)
    - [josephus_problem](algorithms/arrays/josephus.py)
    - [limit](algorithms/arrays/limit.py)
    - [longest_non_repeat](algorithms/arrays/longest_non_repeat.py/)
    - [max_ones_index](algorithms/arrays/max_ones_index.py)
    - [merge_intervals](algorithms/arrays/merge_intervals.py)
    - [missing_ranges](algorithms/arrays/missing_ranges.py)
    - [plus_one](algorithms/arrays/plus_one.py)
    - [rotate](algorithms/arrays/rotate.py)
    - [summarize_ranges](algorithms/arrays/summarize_ranges.py)
    - [three_sum](algorithms/arrays/three_sum.py)
    - [trimmean](algorithms/arrays/trimmean.py)
    - [top_1](algorithms/arrays/top_1.py)
    - [two_sum](algorithms/arrays/two_sum.py)
    - [move_zeros](algorithms/arrays/move_zeros.py)
    - [n_sum](algorithms/arrays/n_sum.py)
- [backtrack](algorithms/backtrack)
    - [general_solution.md](algorithms/backtrack/)
    - [add_operators](algorithms/backtrack/add_operators.py)
    - [anagram](algorithms/backtrack/anagram.py)
    - [array_sum_combinations](algorithms/backtrack/array_sum_combinations.py)
    - [combination_sum](algorithms/backtrack/combination_sum.py)
    - [factor_combinations](algorithms/backtrack/factor_combinations.py)
    - [generate_abbreviations](algorithms/backtrack/generate_abbreviations.py)
    - [generate_parenthesis](algorithms/backtrack/generate_parenthesis.py)
    - [letter_combination](algorithms/backtrack/letter_combination.py)
    - [palindrome_partitioning](algorithms/backtrack/palindrome_partitioning.py)
    - [pattern_match](algorithms/backtrack/pattern_match.py)
    - [permute](algorithms/backtrack/permute.py)
    - [permute_unique](algorithms/backtrack/permute_unique.py)
    - [subsets](algorithms/backtrack/subsets.py)
    - [subsets_unique](algorithms/backtrack/subsets_unique.py)
- [bfs](algorithms/bfs)
    - [maze_search](algorithms/bfs/maze_search.py)
    - [shortest_distance_from_all_buildings](algorithms/bfs/shortest_distance_from_all_buildings.py)
    - [word_ladder](algorithms/bfs/word_ladder.py)
- [bit](algorithms/bit)
    - [add_bitwise_operator](algorithms/bit/add_bitwise_operator.py)
    - [bit_operation](algorithms/bit/bit_operation.py)
    - [bytes_int_conversion](algorithms/bit/bytes_int_conversion.py)
    - [count_flips_to_convert](algorithms/bit/count_flips_to_convert.py)
    - [count_ones](algorithms/bit/count_ones.py)
    - [find_difference](algorithms/bit/find_difference.py)
    - [find_missing_number](algorithms/bit/find_missing_number.py)
    - [flip_bit_longest_sequence](algorithms/bit/flip_bit_longest_sequence.py)
    - [power_of_two](algorithms/bit/power_of_two.py)
    - [reverse_bits](algorithms/bit/reverse_bits.py)
    - [single_number](algorithms/bit/single_number.py)
    - [single_number2](algorithms/bit/single_number2.py)
    - [single_number3](algorithms/bit/single_number3.py)
    - [subsets](algorithms/bit/subsets.py)
    - [swap_pair](algorithms/bit/swap_pair.py)
    - [has_alternative_bit](algorithms/bit/has_alternative_bit.py)
    - [insert_bit](algorithms/bit/insert_bit.py)
    - [remove_bit](algorithms/bit/remove_bit.py)
    - [binary_gap](algorithms/bit/binary_gap.py)
- [calculator](algorithms/calculator)
    - [math_parser](algorithms/calculator/math_parser.py)
- [compression](algorithms/compression)
    - [huffman_coding](algorithms/compression/huffman_coding.py)
    - [rle_compression](algorithms/compression/rle_compression.py)
    - [elias](algorithms/compression/elias.py)
- [dfs](algorithms/dfs)
    - [all_factors](algorithms/dfs/all_factors.py)
    - [count_islands](algorithms/dfs/count_islands.py)
    - [pacific_atlantic](algorithms/dfs/pacific_atlantic.py)
    - [sudoku_solver](algorithms/dfs/sudoku_solver.py)
    - [walls_and_gates](algorithms/dfs/walls_and_gates.py)
- [distribution](algorithms/distribution)
    - [histogram](algorithms/distribution/histogram.py)
- [dp](algorithms/dp)
    - [buy_sell_stock](algorithms/dp/buy_sell_stock.py)
    - [climbing_stairs](algorithms/dp/climbing_stairs.py)
    - [coin_change](algorithms/dp/coin_change.py)
    - [combination_sum](algorithms/dp/combination_sum.py)
    - [egg_drop](algorithms/dp/egg_drop.py)
    - [house_robber](algorithms/dp/house_robber.py)
    - [int_divide](algorithms/dp/int_divide.py)
    - [job_scheduling](algorithms/dp/job_scheduling.py)
    - [knapsack](algorithms/dp/knapsack.py)
    - [longest_increasing](algorithms/dp/longest_increasing.py)
    - [matrix_chain_order](algorithms/dp/matrix_chain_order.py)
    - [max_product_subarray](algorithms/dp/max_product_subarray.py)
    - [max_subarray](algorithms/dp/max_subarray.py)
    - [min_cost_path](algorithms/dp/min_cost_path.py)
    - [num_decodings](algorithms/dp/num_decodings.py)
    - [regex_matching](algorithms/dp/regex_matching.py)
    - [rod_cut](algorithms/dp/rod_cut.py)
    - [word_break](algorithms/dp/word_break.py)
    - [fibonacci](algorithms/dp/fib.py)
	- [hosoya triangle](algorithms/dp/hosoya_triangle.py)
- [graph](algorithms/graph)
    - [check_bipartite](algorithms/graph/check_bipartite.py)
    - [strongly_connected](algorithms/graph/check_digraph_strongly_connected.py)
    - [clone_graph](algorithms/graph/clone_graph.py)
    - [cycle_detection](algorithms/graph/cycle_detection.py)
    - [find_all_cliques](algorithms/graph/find_all_cliques.py)
    - [find_path](algorithms/graph/find_path.py)
    - [graph](algorithms/graph/graph.py)
    - [dijkstra](algorithms/graph/dijkstra.py)
    - [markov_chain](algorithms/graph/markov_chain.py)
    - [minimum_spanning_tree](algorithms/graph/minimum_spanning_tree.py)
    - [satisfiability](algorithms/graph/satisfiability.py)
    - [tarjan](algorithms/graph/tarjan.py)
    - [traversal](algorithms/graph/traversal.py)
- [heap](algorithms/heap)
    - [merge_sorted_k_lists](algorithms/heap/merge_sorted_k_lists.py)
    - [skyline](algorithms/heap/skyline.py)
    - [sliding_window_max](algorithms/heap/sliding_window_max.py)
    - [binary_heap](algorithms/heap/binary_heap.py)
- [iterables](algorithms/iterables)
    - [convolved](algorithms/iterables/convolved.py)
    - [k_closest_points](algorithms/heap/k_closest_points.py)
- [linkedlist](algorithms/linkedlist)
    - [add_two_numbers](algorithms/linkedlist/add_two_numbers.py)
    - [copy_random_pointer](algorithms/linkedlist/copy_random_pointer.py)
    - [delete_node](algorithms/linkedlist/delete_node.py)
    - [first_cyclic_node](algorithms/linkedlist/first_cyclic_node.py)
    - [is_cyclic](algorithms/linkedlist/is_cyclic.py)
    - [is_palindrome](algorithms/linkedlist/is_palindrome.py)
    - [kth_to_last](algorithms/linkedlist/kth_to_last.py)
    - [linkedlist](algorithms/linkedlist/linkedlist.py)
    - [remove_duplicates](algorithms/linkedlist/remove_duplicates.py)
    - [reverse](algorithms/linkedlist/reverse.py)
    - [rotate_list](algorithms/linkedlist/rotate_list.py)
    - [swap_in_pairs](algorithms/linkedlist/swap_in_pairs.py)
    - [is_sorted](algorithms/linkedlist/is_sorted.py)
    - [remove_range](algorithms/linkedlist/remove_range.py)
- [map](algorithms/map)
    - [hashtable](algorithms/map/hashtable.py)
    - [separate_chaining_hashtable](algorithms/map/separate_chaining_hashtable.py)
    - [longest_common_subsequence](algorithms/map/longest_common_subsequence.py)
    - [randomized_set](algorithms/map/randomized_set.py)
    - [valid_sudoku](algorithms/map/valid_sudoku.py)
    - [word_pattern](algorithms/map/word_pattern.py)
    - [is_isomorphic](algorithms/map/is_isomorphic.py)
    - [is_anagram](algorithms/map/is_anagram.py)    
- [maths](algorithms/maths)
    - [base_conversion](algorithms/maths/base_conversion.py)
    - [combination](algorithms/maths/combination.py)
    - [cosine_similarity](algorithms/maths/cosine_similarity.py)
    - [decimal_to_binary_ip](algorithms/maths/decimal_to_binary_ip.py)
    - [euler_totient](algorithms/maths/euler_totient.py)
    - [extended_gcd](algorithms/maths/extended_gcd.py)
    - [factorial](algorithms/maths/factorial.py)    
    - [gcd/lcm](algorithms/maths/gcd.py)
    - [strobogrammtics](algorithms/maths/strobogrammtics.py)
    - [is_strobogrammatic](algorithms/maths/is_strobogrammatic.py)
    - [modular_exponential](algorithms/maths/modular_exponential.py)
    - [next_bigger](algorithms/maths/next_bigger.py)
    - [next_perfect_square](algorithms/maths/next_perfect_square.py)
    - [nth_digit](algorithms/maths/nth_digit.py)
    - [prime_check](algorithms/maths/prime_check.py)
    - [primes_sieve_of_eratosthenes](algorithms/maths/primes_sieve_of_eratosthenes.py)
    - [pythagoras](algorithms/maths/pythagoras.py)
    - [rabin_miller](algorithms/maths/rabin_miller.py)
    - [rsa](algorithms/maths/rsa.py)
    - [sqrt_precision_factor](algorithms/maths/sqrt_precision_factor.py)
    - [summing_digits](algorithms/maths/summing_digits.py)
    - [hailstone](algorithms/maths/hailstone.py)
- [matrix](algorithms/matrix)
    - [sudoku_validator](algorithms/matrix/sudoku_validator.py)
    - [bomb_enemy](algorithms/matrix/bomb_enemy.py)
    - [copy_transform](algorithms/matrix/copy_transform.py)
    - [count_paths](algorithms/matrix/count_paths.py)
    - [matrix_rotation.txt](algorithms/matrix/matrix_rotation.txt)
    - [matrix_multiplication](algorithms/matrix/multiply.py)
    - [rotate_image](algorithms/matrix/rotate_image.py)
    - [search_in_sorted_matrix](algorithms/matrix/search_in_sorted_matrix.py)
    - [sparse_dot_vector](algorithms/matrix/sparse_dot_vector.py)
    - [sparse_mul](algorithms/matrix/sparse_mul.py)
    - [spiral_traversal](algorithms/matrix/spiral_traversal.py)
	- [crout_matrix_decomposition](algorithms/matrix/crout_matrix_decomposition.py)
	- [cholesky_matrix_decomposition](algorithms/matrix/cholesky_matrix_decomposition.py)
- [queues](algorithms/queues)
    - [max_sliding_window](algorithms/queues/max_sliding_window.py)
    - [moving_average](algorithms/queues/moving_average.py)
    - [queue](algorithms/queues/queue.py)
    - [reconstruct_queue](algorithms/queues/reconstruct_queue.py)
    - [zigzagiterator](algorithms/queues/zigzagiterator.py)
- [search](algorithms/search)
    - [binary_search](algorithms/search/binary_search.py)
    - [first_occurrence](algorithms/search/first_occurrence.py)
    - [last_occurrence](algorithms/search/last_occurrence.py)
    - [linear_search](algorithms/search/linear_search.py)
    - [search_insert](algorithms/search/search_insert.py)
    - [two_sum](algorithms/search/two_sum.py)
    - [search_range](algorithms/search/search_range.py)
    - [find_min_rotate](algorithms/search/find_min_rotate.py)
    - [search_rotate](algorithms/search/search_rotate.py)
    - [jump_search](algorithms/search/jump_search.py)
    - [next_greatest_letter](algorithms/search/next_greatest_letter.py)
- [set](algorithms/set)
    - [randomized_set](algorithms/set/randomized_set.py)
    - [set_covering](algorithms/set/set_covering.py)
    - [find_keyboard_row](algorithms/set/find_keyboard_row.py)
- [sort](algorithms/sort)
    - [bitonic_sort](algorithms/sort/bitonic_sort.py)
    - [bogo_sort](algorithms/sort/bogo_sort.py)
    - [bubble_sort](algorithms/sort/bubble_sort.py)
    - [bucket_sort](algorithms/sort/bucket_sort.py)
    - [cocktail_shaker_sort](algorithms/sort/cocktail_shaker_sort.py)
    - [comb_sort](algorithms/sort/comb_sort.py)
    - [counting_sort](algorithms/sort/counting_sort.py)
    - [cycle_sort](algorithms/sort/cycle_sort.py)
    - [gnome_sort](algorithms/sort/gnome_sort.py)
    - [heap_sort](algorithms/sort/heap_sort.py)
    - [insertion_sort](algorithms/sort/insertion_sort.py)
    - [meeting_rooms](algorithms/sort/meeting_rooms.py)
    - [merge_sort](algorithms/sort/merge_sort.py)
    - [pancake_sort](algorithms/sort/pancake_sort.py)
    - [quick_sort](algorithms/sort/quick_sort.py)
    - [radix_sort](algorithms/sort/radix_sort.py)
    - [selection_sort](algorithms/sort/selection_sort.py)
    - [shell_sort](algorithms/sort/shell_sort.py)
    - [sort_colors](algorithms/sort/sort_colors.py)
    - [top_sort](algorithms/sort/top_sort.py)
    - [wiggle_sort](algorithms/sort/wiggle_sort.py)
- [stack](algorithms/stack)
    - [longest_abs_path](algorithms/stack/longest_abs_path.py)
    - [simplify_path](algorithms/stack/simplify_path.py)
    - [stack](algorithms/stack/stack.py)
    - [valid_parenthesis](algorithms/stack/valid_parenthesis.py)
    - [stutter](algorithms/stack/stutter.py)
    - [switch_pairs](algorithms/stack/switch_pairs.py)
    - [is_consecutive](algorithms/stack/is_consecutive.py)
    - [remove_min](algorithms/stack/remove_min.py)
    - [is_sorted](algorithms/stack/is_sorted.py)
- [strings](algorithms/strings)
    - [fizzbuzz](algorithms/strings/fizzbuzz.py)
    - [delete_reoccurring](algorithms/strings/delete_reoccurring.py)
    - [strip_url_params](algorithms/strings/strip_url_params.py)
    - [validate_coordinates](algorithms/strings/validate_coordinates.py)
    - [domain_extractor](algorithms/strings/domain_extractor.py)
    - [merge_string_checker](algorithms/strings/merge_string_checker.py)
    - [add_binary](algorithms/strings/add_binary.py)
    - [breaking_bad](algorithms/strings/breaking_bad.py)
    - [decode_string](algorithms/strings/decode_string.py)
    - [encode_decode](algorithms/strings/encode_decode.py)
    - [group_anagrams](algorithms/strings/group_anagrams.py)
    - [int_to_roman](algorithms/strings/int_to_roman.py)
    - [is_palindrome](algorithms/strings/is_palindrome.py)
    - [license_number](algorithms/strings/license_number.py)
    - [make_sentence](algorithms/strings/make_sentence.py)
    - [multiply_strings](algorithms/strings/multiply_strings.py)
    - [one_edit_distance](algorithms/strings/one_edit_distance.py)
    - [rabin_karp](algorithms/strings/rabin_karp.py)
    - [reverse_string](algorithms/strings/reverse_string.py)
    - [reverse_vowel](algorithms/strings/reverse_vowel.py)
    - [reverse_words](algorithms/strings/reverse_words.py)
    - [roman_to_int](algorithms/strings/roman_to_int.py)
    - [word_squares](algorithms/strings/word_squares.py)
    - [unique_morse](algorithms/strings/unique_morse.py)
    - [judge_circle](algorithms/strings/judge_circle.py)
    - [strong_password](algorithms/strings/strong_password.py)
    - [caesar_cipher](algorithms/strings/caesar_cipher.py)
    - [contain_string](algorithms/strings/contain_string.py)
    - [count_binary_substring](algorithms/strings/count_binary_substring.py)
    - [repeat_string](algorithms/strings/repeat_string.py)
    - [min_distance](algorithms/strings/min_distance.py)
    - [longest_common_prefix](algorithms/strings/longest_common_prefix.py)
    - [rotate](algorithms/strings/rotate.py)
    - [first_unique_char](algorithms/strings/first_unique_char.py)
    - [repeat_substring](algorithms/strings/repeat_substring.py)     
	- [atbash_cipher](algorithms/strings/atbash_cipher.py)
- [tree](algorithms/tree)
    - [bst](algorithms/tree/bst)
        - [array_to_bst](algorithms/tree/bst/array_to_bst.py)
        - [bst_closest_value](algorithms/tree/bst/bst_closest_value.py)
        - [BSTIterator](algorithms/tree/bst/BSTIterator.py)
        - [delete_node](algorithms/tree/bst/delete_node.py)
        - [is_bst](algorithms/tree/bst/is_bst.py)
        - [kth_smallest](algorithms/tree/bst/kth_smallest.py)
        - [lowest_common_ancestor](algorithms/tree/bst/lowest_common_ancestor.py)
        - [predecessor](algorithms/tree/bst/predecessor.py)
        - [serialize_deserialize](algorithms/tree/bst/serialize_deserialize.py)
        - [successor](algorithms/tree/bst/successor.py)
        - [unique_bst](algorithms/tree/bst/unique_bst.py)
        - [depth_sum](algorithms/tree/bst/depth_sum.py)
        - [count_left_node](algorithms/tree/bst/count_left_node.py)
        - [num_empty](algorithms/tree/bst/num_empty.py)
        - [height](algorithms/tree/bst/height.py)
    - [red_black_tree](algorithms/tree/red_black_tree)
        - [red_black_tree](algorithms/tree/red_black_tree/red_black_tree.py)
    - [segment_tree](algorithms/tree/segment_tree)
        - [segment_tree](algorithms/tree/segment_tree/segment_tree.py)
        - [iterative_segment_tree](algorithms/tree/segment_tree/iterative_segment_tree.py)
    - [traversal](algorithms/tree/traversal)
        - [inorder](algorithms/tree/traversal/inorder.py)
        - [level_order](algorithms/tree/traversal/level_order.py)
        - [postorder](algorithms/tree/traversal/postorder.py)
        - [preorder](algorithms/tree/traversal/preorder.py)
        - [zigzag](algorithms/tree/traversal/zigzag.py)
    - [trie](algorithms/tree/trie)
        - [add_and_search](algorithms/tree/trie/add_and_search.py)
        - [trie](algorithms/tree/trie/trie.py)
    - [b_tree](algorithms/tree/b_tree.py)
    - [binary_tree_paths](algorithms/tree/binary_tree_paths.py)
    - [bin_tree_to_list](algorithms/tree/bin_tree_to_list.py)
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
    - [tree](algorithms/tree/tree.py)
- [unix](algorithms/unix)
    - [path](algorithms/unix/path/)
        - [join_with_slash](algorithms/unix/path/join_with_slash.py)
        - [full_path](algorithms/unix/path/full_path.py)
        - [split](algorithms/unix/path/split.py)
        - [simplify_path](algorithms/unix/path/simplify_path.py)
- [union-find](algorithms/union-find)
    - [count_islands](algorithms/union-find/count_islands.py)


## Contributors

Thanks to [all the contributors](https://github.com/keon/algorithms/graphs/contributors)
who helped in building the repo.
