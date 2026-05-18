# TRIAGE: library vs examples

Working document for the planned split of `algorithms/` into two top-level
trees:

- `algorithms/` — reusable building blocks (canonical algorithms, data
  structures, named techniques). Continues to ship on PyPI.
- `examples/` — LeetCode/puzzle-style problem solutions. Worked examples
  that consume the library; not part of the importable API surface.

Layout: top-level `examples/` directory.
Backwards compat: **hard break** in the next major release. No shims.
Status: draft — needs your review and overrides before any file moves.

## Decision criteria (3-test)

1. **Reusability** — Would a user `import` this to solve *their own* problem?
   If no → example.
2. **Input framing** — Is the input shape coupled to one specific problem
   (e.g. "2D grid where 1=land, 0=water"; "array of stock prices")?
   If yes → example.
3. **Named algorithm or DS** — Is it a classical, named algorithm (Dijkstra,
   Tarjan, FFT, Floyd-Warshall, KMP, Manacher) or data structure (AVL,
   B-tree, trie, union-find)? If yes → library.

Tiebreaker: *"If this got deleted, would someone copy it to do real work,
or just reimplement it for their own input?"*

## Legend

- 📚 **LIBRARY** — pure, reusable algorithm/DS
- 🧩 **EXAMPLE** — problem-style code, belongs in `examples/`
- ❓ **AMBIGUOUS** — explicit decision needed
- ⚠️ **NOTE** — see end of section for context

## Summary

| Category | Library | Example | Ambiguous |
|---|---:|---:|---:|
| array | 4 | 14 | 1 |
| backtracking | 6 | 8 | 1 |
| bit_manipulation | 7 | 11 | 1 |
| common | 4 | 0 | 0 |
| compression | 3 | 0 | 0 |
| data_structures | 21 | 0 | 0 |
| dynamic_programming | 9 | 15 | 2 |
| graph | 28 | 12 | 1 |
| greedy | 1 | 1 | 0 |
| heap | 1 | 3 | 0 |
| linked_list | 6 | 10 | 0 |
| map | 2 | 5 | 0 |
| math | 32 | 4 | 0 |
| matrix | 6 | 10 | 0 |
| queue | 0 | 4 | 0 |
| searching | 12 | 3 | 1 |
| set | 1 | 2 | 0 |
| sorting | 21 | 2 | 0 |
| stack | 1 | 8 | 0 |
| streaming | 2 | 0 | 0 |
| string | 8 | 32 | 1 |
| tree | 7 | 24 | 1 |
| **Total** | **182** | **164** | **9** |

(Counts are best-effort; the per-category tables below are the source of truth.)

---

## array/

| File | Bucket | Reason |
|---|---|---|
| `delete_nth.py` | 🧩 EXAMPLE | leetcode-style: cap occurrences in a list |
| `flatten.py` | 📚 LIBRARY | canonical utility (flatten nested iterable) |
| `garage.py` | 🧩 EXAMPLE | 15-puzzle / specific parking-lot framing |
| `josephus.py` | 📚 LIBRARY | classical named problem with reusable generator |
| `limit.py` | 🧩 EXAMPLE | array clipping — trivial filter, leetcode-style |
| `longest_non_repeat.py` | 🧩 EXAMPLE | leetcode "longest substring without repeating" |
| `max_ones_index.py` | 🧩 EXAMPLE | leetcode-specific |
| `merge_intervals.py` | 📚 LIBRARY | canonical interval-merging routine, widely reusable |
| `missing_ranges.py` | 🧩 EXAMPLE | leetcode |
| `move_zeros.py` | 🧩 EXAMPLE | leetcode (URL in file) |
| `n_sum.py` | 📚 LIBRARY | canonical k-sum technique (reusable closure-based API) |
| `plus_one.py` | 🧩 EXAMPLE | leetcode |
| `remove_duplicates.py` | 🧩 EXAMPLE | leetcode |
| `rotate.py` | 🧩 EXAMPLE | leetcode |
| `summarize_ranges.py` | 🧩 EXAMPLE | leetcode |
| `three_sum.py` | ❓ AMBIGUOUS | leetcode-origin but is *the* canonical two-pointer 3-sum implementation — many users reach for this exact code |
| `top_1.py` | 🧩 EXAMPLE | mode-finding, trivial |
| `trimmean.py` | 🧩 EXAMPLE | trimmed-mean specific framing |
| `two_sum.py` | 📚 LIBRARY | canonical hash-map two-sum (the textbook example of the technique) |

⚠️ Note on three_sum/two_sum/n_sum: they're leetcode-origin but have become
*the* reference implementations for these techniques. I lean library, but
flagging three_sum because some would argue it's a leetcode example.

## backtracking/

| File | Bucket | Reason |
|---|---|---|
| `add_operators.py` | 🧩 EXAMPLE | leetcode "expression add operators" |
| `anagram.py` | 🧩 EXAMPLE | doesn't actually backtrack — just sort/count; misplaced |
| `array_sum_combinations.py` | 🧩 EXAMPLE | leetcode-style |
| `combination_sum.py` | 📚 LIBRARY | canonical backtracking template — combination-sum is widely taught |
| `factor_combinations.py` | 🧩 EXAMPLE | leetcode |
| `find_words.py` | 🧩 EXAMPLE | leetcode "word search II" (trie + backtrack) |
| `generate_abbreviations.py` | 🧩 EXAMPLE | leetcode |
| `generate_parenthesis.py` | 📚 LIBRARY | canonical backtracking textbook example |
| `letter_combination.py` | 📚 LIBRARY | classical phone-letter combinations — canonical |
| `minimax.py` | 📚 LIBRARY | game-tree search with alpha-beta — foundational |
| `palindrome_partitioning.py` | 🧩 EXAMPLE | leetcode |
| `pattern_match.py` | 🧩 EXAMPLE | leetcode "word pattern II" |
| `permute_unique.py` | 📚 LIBRARY | canonical (permutations with duplicates) |
| `permute.py` | 📚 LIBRARY | canonical permutation generation |
| `subsets_unique.py` | ❓ AMBIGUOUS | borderline — canonical subset gen but with dedup leetcode flavor |
| `subsets.py` | 📚 LIBRARY | canonical subset generation |

## bit_manipulation/

| File | Bucket | Reason |
|---|---|---|
| `add_bitwise_operator.py` | 📚 LIBRARY | classical bitwise addition |
| `binary_gap.py` | 🧩 EXAMPLE | Codility/leetcode |
| `bit_operation.py` | 📚 LIBRARY | core bit utilities |
| `bytes_int_conversion.py` | 📚 LIBRARY | reusable conversion helpers |
| `count_flips_to_convert.py` | 🧩 EXAMPLE | leetcode |
| `count_ones.py` | 📚 LIBRARY | Hamming weight / popcount — canonical |
| `find_difference.py` | 🧩 EXAMPLE | leetcode |
| `find_missing_number.py` | 📚 LIBRARY | classical XOR trick — widely taught |
| `flip_bit_longest_sequence.py` | 🧩 EXAMPLE | leetcode |
| `gray_code.py` | 📚 LIBRARY | classical Gray-code generation |
| `has_alternative_bit.py` | 🧩 EXAMPLE | leetcode |
| `insert_bit.py` | 🧩 EXAMPLE | leetcode |
| `power_of_two.py` | 📚 LIBRARY | canonical bit-test |
| `remove_bit.py` | 🧩 EXAMPLE | leetcode |
| `reverse_bits.py` | 📚 LIBRARY | canonical |
| `single_number.py` | 🧩 EXAMPLE | leetcode (XOR-find-unique) |
| `single_number2.py` | 🧩 EXAMPLE | leetcode variant |
| `single_number3.py` | 🧩 EXAMPLE | leetcode variant |
| `subsets.py` | ❓ AMBIGUOUS | bitmask enumeration of subsets — canonical technique; duplicate name with backtracking/subsets.py |
| `swap_pair.py` | 🧩 EXAMPLE | leetcode |

## common/

| File | Bucket | Reason |
|---|---|---|
| `graph.py` | 📚 LIBRARY | shared graph type (used as library type) |
| `linked_list_protocol.py` | 📚 LIBRARY | shared protocol |
| `list_node.py` | 📚 LIBRARY | shared ListNode type |
| `tree_node.py` | 📚 LIBRARY | shared TreeNode type |

## compression/

All 📚 LIBRARY — classical encoding schemes.

| File | Bucket | Reason |
|---|---|---|
| `elias.py` | 📚 LIBRARY | Elias gamma/delta/omega coding |
| `huffman_coding.py` | 📚 LIBRARY | Huffman coding |
| `rle_compression.py` | 📚 LIBRARY | Run-length encoding |

## data_structures/

All 📚 LIBRARY without exception.

| File | Bucket | Reason |
|---|---|---|
| `avl_tree.py` | 📚 LIBRARY | AVL tree |
| `b_tree.py` | 📚 LIBRARY | B-tree |
| `bst.py` | 📚 LIBRARY | BST |
| `fenwick_tree.py` | 📚 LIBRARY | Fenwick tree / BIT |
| `graph.py` | 📚 LIBRARY | graph class |
| `hash_table.py` | 📚 LIBRARY | hash table |
| `heap.py` | 📚 LIBRARY | binary heap |
| `iterative_segment_tree.py` | 📚 LIBRARY | iterative segment tree |
| `kd_tree.py` | 📚 LIBRARY | k-d tree |
| `linked_list.py` | 📚 LIBRARY | linked list |
| `priority_queue.py` | 📚 LIBRARY | priority queue |
| `queue.py` | 📚 LIBRARY | queue variants |
| `red_black_tree.py` | 📚 LIBRARY | red-black tree |
| `segment_tree.py` | 📚 LIBRARY | segment tree |
| `separate_chaining_hash_table.py` | 📚 LIBRARY | hash table variant |
| `sqrt_decomposition.py` | 📚 LIBRARY | sqrt decomposition |
| `stack.py` | 📚 LIBRARY | stack |
| `trie.py` | 📚 LIBRARY | trie |
| `union_find.py` | 📚 LIBRARY | union-find / DSU |
| `veb_tree.py` | 📚 LIBRARY | van Emde Boas tree |

## dynamic_programming/

| File | Bucket | Reason |
|---|---|---|
| `bitmask.py` | 📚 LIBRARY | canonical bitmask DP template |
| `buy_sell_stock.py` | 🧩 EXAMPLE | leetcode (stock-price story) |
| `climbing_stairs.py` | 🧩 EXAMPLE | leetcode (textbook intro DP but tied to a story) |
| `coin_change.py` | 📚 LIBRARY | canonical DP — widely reused |
| `combination_sum.py` | ❓ AMBIGUOUS | borderline; duplicate name with backtracking/combination_sum |
| `count_paths_dp.py` | 🧩 EXAMPLE | leetcode "unique paths" |
| `edit_distance.py` | 📚 LIBRARY | classical Levenshtein |
| `egg_drop.py` | 📚 LIBRARY | classical egg-drop DP |
| `fib.py` | 📚 LIBRARY | Fibonacci — canonical DP intro |
| `hosoya_triangle.py` | 🧩 EXAMPLE | specific sequence |
| `house_robber.py` | 🧩 EXAMPLE | leetcode (house story) |
| `int_divide.py` | 🧩 EXAMPLE | integer partition variant |
| `job_scheduling.py` | 📚 LIBRARY | classical weighted job scheduling |
| `k_factor.py` | 🧩 EXAMPLE | competitive-programming problem |
| `knapsack.py` | 📚 LIBRARY | classical knapsack |
| `longest_common_subsequence.py` | 📚 LIBRARY | classical LCS |
| `longest_increasing.py` | 📚 LIBRARY | classical LIS |
| `matrix_chain_order.py` | 📚 LIBRARY | classical matrix-chain multiplication |
| `max_product_subarray.py` | 🧩 EXAMPLE | leetcode |
| `max_subarray.py` | ❓ AMBIGUOUS | Kadane's algorithm — canonical, but the variant here is leetcode-flavored |
| `min_cost_path.py` | 🧩 EXAMPLE | grid DP |
| `num_decodings.py` | 🧩 EXAMPLE | leetcode |
| `planting_trees.py` | 🧩 EXAMPLE | specific problem |
| `regex_matching.py` | 🧩 EXAMPLE | leetcode |
| `rod_cut.py` | 📚 LIBRARY | classical CLRS rod-cutting |
| `word_break.py` | 🧩 EXAMPLE | leetcode |

## graph/

| File | Bucket | Reason |
|---|---|---|
| `a_star.py` | 📚 LIBRARY | A* search |
| `all_factors.py` | 🧩 EXAMPLE | number-theory listing (mis-placed in graph) |
| `all_pairs_shortest_path.py` | 📚 LIBRARY | Floyd-Warshall |
| `bellman_ford.py` | 📚 LIBRARY | Bellman-Ford |
| `blossom.py` | 📚 LIBRARY | Edmonds' blossom matching |
| `check_bipartite.py` | 📚 LIBRARY | classical bipartite check |
| `check_digraph_strongly_connected.py` | 📚 LIBRARY | classical SCC check |
| `clone_graph.py` | 🧩 EXAMPLE | leetcode |
| `count_connected_number_of_component.py` | 📚 LIBRARY | classical connected components |
| `count_islands_bfs.py` | 🧩 EXAMPLE | leetcode "number of islands" (BFS variant) |
| `count_islands_dfs.py` | 🧩 EXAMPLE | leetcode (DFS variant) |
| `count_islands_unionfind.py` | 🧩 EXAMPLE | leetcode (UF variant) |
| `cycle_detection.py` | 📚 LIBRARY | classical cycle detection |
| `dijkstra_heapq.py` | 📚 LIBRARY | Dijkstra (heap-based) |
| `dijkstra.py` | 📚 LIBRARY | Dijkstra |
| `find_all_cliques.py` | 📚 LIBRARY | Bron-Kerbosch (classical) |
| `find_path.py` | 📚 LIBRARY | generic path-finding |
| `graph.py` | 📚 LIBRARY | base graph type |
| `kahns_algorithm.py` | 📚 LIBRARY | Kahn's topological sort |
| `markov_chain.py` | 📚 LIBRARY | Markov chain simulation |
| `maximum_flow_bfs.py` | 📚 LIBRARY | Edmonds-Karp |
| `maximum_flow_dfs.py` | 📚 LIBRARY | Ford-Fulkerson DFS |
| `maximum_flow.py` | 📚 LIBRARY | max-flow base |
| `maze_search_bfs.py` | 📚 LIBRARY | canonical maze BFS |
| `maze_search_dfs.py` | 📚 LIBRARY | canonical maze DFS |
| `minimum_spanning_tree.py` | 📚 LIBRARY | Kruskal/Prim |
| `pacific_atlantic.py` | 🧩 EXAMPLE | leetcode |
| `path_between_two_vertices_in_digraph.py` | 📚 LIBRARY | reachability |
| `prims_minimum_spanning.py` | 📚 LIBRARY | Prim's |
| `satisfiability.py` | 📚 LIBRARY | 2-SAT |
| `shortest_distance_from_all_buildings.py` | 🧩 EXAMPLE | leetcode |
| `strongly_connected_components_kosaraju.py` | 📚 LIBRARY | Kosaraju's SCC |
| `sudoku_solver.py` | ❓ AMBIGUOUS | classical CSP example but tied to sudoku |
| `tarjan.py` | 📚 LIBRARY | Tarjan's SCC |
| `topological_sort_bfs.py` | 📚 LIBRARY | topological sort (BFS) |
| `topological_sort_dfs.py` | 📚 LIBRARY | topological sort (DFS) |
| `transitive_closure_dfs.py` | 📚 LIBRARY | transitive closure |
| `traversal.py` | 📚 LIBRARY | BFS/DFS templates |
| `walls_and_gates.py` | 🧩 EXAMPLE | leetcode (URL in file) |
| `word_ladder.py` | 🧩 EXAMPLE | leetcode |

## greedy/

| File | Bucket | Reason |
|---|---|---|
| `gale_shapley.py` | 📚 LIBRARY | Gale-Shapley stable matching |
| `max_contiguous_subsequence_sum.py` | 🧩 EXAMPLE | leetcode (overlaps with Kadane in DP) |

## heap/

| File | Bucket | Reason |
|---|---|---|
| `k_closest_points.py` | 🧩 EXAMPLE | leetcode |
| `merge_sorted_k_lists.py` | 🧩 EXAMPLE | leetcode |
| `skyline.py` | 📚 LIBRARY | classical skyline problem (sweep line) |
| `sliding_window_max.py` | 🧩 EXAMPLE | leetcode |

## linked_list/

Most operations here ARE the canonical linked-list techniques. Splitting
finer than "BST ops vs LeetCode problems":

| File | Bucket | Reason |
|---|---|---|
| `add_two_numbers.py` | 🧩 EXAMPLE | leetcode |
| `copy_random_pointer.py` | 🧩 EXAMPLE | leetcode |
| `delete_node.py` | 🧩 EXAMPLE | leetcode |
| `first_cyclic_node.py` | 📚 LIBRARY | Floyd's cycle detection — canonical |
| `intersection.py` | 🧩 EXAMPLE | leetcode |
| `is_cyclic.py` | 📚 LIBRARY | canonical cycle check |
| `is_palindrome.py` | 🧩 EXAMPLE | leetcode |
| `is_sorted.py` | 📚 LIBRARY | basic property check |
| `kth_to_last.py` | 📚 LIBRARY | classical two-pointer technique |
| `merge_two_list.py` | 📚 LIBRARY | canonical merge |
| `partition.py` | 🧩 EXAMPLE | leetcode |
| `remove_duplicates.py` | 🧩 EXAMPLE | leetcode |
| `remove_range.py` | 🧩 EXAMPLE | leetcode |
| `reverse.py` | 📚 LIBRARY | canonical linked-list reversal |
| `rotate_list.py` | 🧩 EXAMPLE | leetcode |
| `swap_in_pairs.py` | 🧩 EXAMPLE | leetcode |

## map/

| File | Bucket | Reason |
|---|---|---|
| `is_anagram.py` | 🧩 EXAMPLE | leetcode (anagram check via counter) |
| `is_isomorphic.py` | 🧩 EXAMPLE | leetcode |
| `longest_common_substring.py` | 📚 LIBRARY | classical LCS-substring (was the misnamed file we fixed) |
| `longest_palindromic_subsequence.py` | 📚 LIBRARY | classical |
| `randomized_set.py` | 🧩 EXAMPLE | leetcode "insert/delete/getRandom O(1)" |
| `valid_sudoku.py` | 🧩 EXAMPLE | leetcode |
| `word_pattern.py` | 🧩 EXAMPLE | leetcode |

## math/

The bulk is classical math. Mostly library.

| File | Bucket | Reason |
|---|---|---|
| `base_conversion.py` | 📚 LIBRARY | canonical |
| `chebyshev_distance.py` | 📚 LIBRARY | L∞ distance metric |
| `chinese_remainder_theorem.py` | 📚 LIBRARY | CRT |
| `combination.py` | 📚 LIBRARY | nCr |
| `cosine_similarity.py` | 📚 LIBRARY | cosine sim |
| `decimal_to_binary_ip.py` | 🧩 EXAMPLE | specific IP-conversion problem |
| `diffie_hellman_key_exchange.py` | 📚 LIBRARY | DH |
| `distance_between_two_points.py` | 📚 LIBRARY | Euclidean distance |
| `euler_totient.py` | 📚 LIBRARY | φ(n) |
| `extended_gcd.py` | 📚 LIBRARY | extended Euclidean |
| `factorial.py` | 📚 LIBRARY | n! |
| `fft.py` | 📚 LIBRARY | Fast Fourier transform |
| `find_order_simple.py` | 📚 LIBRARY | multiplicative order |
| `find_primitive_root_simple.py` | 📚 LIBRARY | primitive root |
| `gcd.py` | 📚 LIBRARY | Euclidean GCD |
| `generate_strobogrammtic.py` | 🧩 EXAMPLE | leetcode |
| `geometric_mean.py` | 📚 LIBRARY | geometric mean |
| `goldbach.py` | 📚 LIBRARY | Goldbach decomposition |
| `hailstone.py` | 📚 LIBRARY | Collatz/hailstone |
| `is_strobogrammatic.py` | 🧩 EXAMPLE | leetcode |
| `krishnamurthy_number.py` | 📚 LIBRARY | classical recreational |
| `linear_regression.py` | 📚 LIBRARY | linear regression |
| `magic_number.py` | 📚 LIBRARY | magic-number test |
| `manhattan_distance.py` | 📚 LIBRARY | L1 distance |
| `modular_exponential.py` | 📚 LIBRARY | fast modular exp |
| `modular_inverse.py` | 📚 LIBRARY | modular inverse |
| `next_bigger.py` | 🧩 EXAMPLE | leetcode "next greater number" |
| `next_perfect_square.py` | 📚 LIBRARY | trivial but reusable |
| `nth_digit.py` | 📚 LIBRARY | digit indexing |
| `num_digits.py` | 📚 LIBRARY | digit count |
| `num_perfect_squares.py` | 📚 LIBRARY | Lagrange four-square (DP variant) |
| `polynomial_division.py` | 📚 LIBRARY | polynomial division |
| `polynomial.py` | 📚 LIBRARY | polynomial class |
| `power.py` | 📚 LIBRARY | fast exponentiation |
| `prime_check.py` | 📚 LIBRARY | primality |
| `primes_sieve_of_eratosthenes.py` | 📚 LIBRARY | sieve |
| `pythagoras.py` | 📚 LIBRARY | Pythagorean triple test |
| `rabin_miller.py` | 📚 LIBRARY | Miller-Rabin |
| `recursive_binomial_coefficient.py` | 📚 LIBRARY | recursive nCr |
| `rsa.py` | 📚 LIBRARY | RSA |
| `sqrt_precision_factor.py` | 📚 LIBRARY | sqrt to precision |
| `summing_digits.py` | 📚 LIBRARY | digit-sum |
| `surface_area_of_torus.py` | 📚 LIBRARY | geometry |
| `symmetry_group_cycle_index.py` | 📚 LIBRARY | Pólya enumeration |

## matrix/

| File | Bucket | Reason |
|---|---|---|
| `bomb_enemy.py` | 🧩 EXAMPLE | leetcode |
| `cholesky_matrix_decomposition.py` | 📚 LIBRARY | classical |
| `copy_transform.py` | 🧩 EXAMPLE | specific transform |
| `count_paths.py` | 🧩 EXAMPLE | grid-DP variant |
| `crout_matrix_decomposition.py` | 📚 LIBRARY | LU (Crout) |
| `matrix_exponentiation.py` | 📚 LIBRARY | fast matrix power |
| `matrix_inversion.py` | 📚 LIBRARY | matrix inverse |
| `multiply.py` | 📚 LIBRARY | matrix multiply |
| `rotate_image.py` | 🧩 EXAMPLE | leetcode |
| `search_in_sorted_matrix.py` | 🧩 EXAMPLE | leetcode |
| `sort_matrix_diagonally.py` | 🧩 EXAMPLE | leetcode |
| `sparse_dot_vector.py` | 🧩 EXAMPLE | leetcode |
| `sparse_mul.py` | 🧩 EXAMPLE | leetcode |
| `spiral_traversal.py` | 🧩 EXAMPLE | leetcode |
| `sudoku_validator.py` | 🧩 EXAMPLE | leetcode (validate sudoku board) |
| `sum_sub_squares.py` | 📚 LIBRARY | submatrix sum (canonical prefix-sum) |

## queue/

| File | Bucket | Reason |
|---|---|---|
| `max_sliding_window.py` | 🧩 EXAMPLE | leetcode |
| `moving_average.py` | 🧩 EXAMPLE | leetcode |
| `reconstruct_queue.py` | 🧩 EXAMPLE | leetcode |
| `zigzagiterator.py` | 🧩 EXAMPLE | leetcode |

## searching/

| File | Bucket | Reason |
|---|---|---|
| `binary_search.py` | 📚 LIBRARY | binary search |
| `exponential_search.py` | 📚 LIBRARY | exponential search |
| `find_min_rotate.py` | 🧩 EXAMPLE | leetcode "min in rotated sorted array" |
| `first_occurrence.py` | 📚 LIBRARY | leftmost binary search |
| `generalized_binary_search.py` | 📚 LIBRARY | predicate-based binary search |
| `interpolation_search.py` | 📚 LIBRARY | interpolation search |
| `jump_search.py` | 📚 LIBRARY | jump search |
| `last_occurrence.py` | 📚 LIBRARY | rightmost binary search |
| `linear_search.py` | 📚 LIBRARY | linear search |
| `next_greatest_letter.py` | 🧩 EXAMPLE | leetcode |
| `search_insert.py` | 📚 LIBRARY | binary search insert position |
| `search_range.py` | 📚 LIBRARY | first/last in sorted array |
| `search_rotate.py` | ❓ AMBIGUOUS | leetcode-origin but is *the* canonical rotated-binary-search |
| `sentinel_search.py` | 📚 LIBRARY | sentinel linear search |
| `ternary_search.py` | 📚 LIBRARY | ternary search |
| `two_sum.py` | 📚 LIBRARY | canonical 2-sum on sorted array (binary search / two-pointer); see duplicate-name note below |

⚠️ Note: `searching/two_sum.py` and `array/two_sum.py` are different
implementations of the same problem. Consider consolidating during the
move (keep both as variants in `algorithms/algorithms/array/two_sum.py`,
or split into `two_sum_hash.py` and `two_sum_sorted.py`).

## set/

| File | Bucket | Reason |
|---|---|---|
| `find_keyboard_row.py` | 🧩 EXAMPLE | leetcode |
| `randomized_set.py` | 🧩 EXAMPLE | leetcode (duplicate of `map/randomized_set.py`?) |
| `set_covering.py` | 📚 LIBRARY | classical set cover (NP-complete, taught widely) |

⚠️ Note: `set/randomized_set.py` and `map/randomized_set.py` may be the
same algorithm in two locations. Worth checking during the move.

## sorting/

Almost all named sorts → LIBRARY.

| File | Bucket | Reason |
|---|---|---|
| `bead_sort.py` | 📚 LIBRARY | bead sort |
| `bitonic_sort.py` | 📚 LIBRARY | bitonic sort |
| `bogo_sort.py` | 📚 LIBRARY | bogo sort |
| `bubble_sort.py` | 📚 LIBRARY | bubble sort |
| `bucket_sort.py` | 📚 LIBRARY | bucket sort |
| `cocktail_shaker_sort.py` | 📚 LIBRARY | cocktail-shaker sort |
| `comb_sort.py` | 📚 LIBRARY | comb sort |
| `counting_sort.py` | 📚 LIBRARY | counting sort |
| `cycle_sort.py` | 📚 LIBRARY | cycle sort |
| `exchange_sort.py` | 📚 LIBRARY | exchange sort |
| `gnome_sort.py` | 📚 LIBRARY | gnome sort |
| `heap_sort.py` | 📚 LIBRARY | heap sort |
| `insertion_sort.py` | 📚 LIBRARY | insertion sort |
| `meeting_rooms.py` | 🧩 EXAMPLE | leetcode |
| `merge_sort.py` | 📚 LIBRARY | merge sort |
| `pancake_sort.py` | 📚 LIBRARY | pancake sort |
| `pigeonhole_sort.py` | 📚 LIBRARY | pigeonhole sort |
| `quick_sort.py` | 📚 LIBRARY | quicksort |
| `radix_sort.py` | 📚 LIBRARY | radix sort |
| `selection_sort.py` | 📚 LIBRARY | selection sort |
| `shell_sort.py` | 📚 LIBRARY | shell sort |
| `sort_colors.py` | 🧩 EXAMPLE | leetcode (Dutch national flag — borderline; canonical name but leetcode flavor) |
| `stooge_sort.py` | 📚 LIBRARY | stooge sort |
| `wiggle_sort.py` | 🧩 EXAMPLE | leetcode |

## stack/

| File | Bucket | Reason |
|---|---|---|
| `is_consecutive.py` | 🧩 EXAMPLE | specific stack-question |
| `is_sorted.py` | 🧩 EXAMPLE | specific stack-question |
| `longest_abs_path.py` | 🧩 EXAMPLE | leetcode |
| `ordered_stack.py` | 🧩 EXAMPLE | specific stack-question |
| `remove_min.py` | 🧩 EXAMPLE | specific |
| `simplify_path.py` | 🧩 EXAMPLE | leetcode |
| `stutter.py` | 🧩 EXAMPLE | specific stack-question |
| `switch_pairs.py` | 🧩 EXAMPLE | specific |
| `valid_parenthesis.py` | 📚 LIBRARY | canonical balanced-parens (textbook) |

## streaming/

| File | Bucket | Reason |
|---|---|---|
| `misra_gries.py` | 📚 LIBRARY | Misra-Gries heavy hitters |
| `one_sparse_recovery.py` | 📚 LIBRARY | streaming algorithm |

## string/

The string folder has the most LeetCode examples.

| File | Bucket | Reason |
|---|---|---|
| `add_binary.py` | 🧩 EXAMPLE | leetcode |
| `alphabet_board_path.py` | 🧩 EXAMPLE | leetcode |
| `atbash_cipher.py` | 📚 LIBRARY | Atbash cipher |
| `breaking_bad.py` | 🧩 EXAMPLE | thematic puzzle |
| `caesar_cipher.py` | 📚 LIBRARY | Caesar cipher |
| `check_pangram.py` | 🧩 EXAMPLE | leetcode |
| `contain_string.py` | 🧩 EXAMPLE | leetcode strStr |
| `count_binary_substring.py` | 🧩 EXAMPLE | leetcode |
| `decode_string.py` | 🧩 EXAMPLE | leetcode |
| `delete_reoccurring.py` | 🧩 EXAMPLE | leetcode |
| `domain_extractor.py` | 🧩 EXAMPLE | leetcode |
| `encode_decode.py` | 🧩 EXAMPLE | leetcode |
| `first_unique_char.py` | 🧩 EXAMPLE | leetcode |
| `fizzbuzz.py` | 🧩 EXAMPLE | classic warmup |
| `group_anagrams.py` | 🧩 EXAMPLE | leetcode |
| `int_to_roman.py` | 📚 LIBRARY | classical roman-numeral conversion |
| `is_palindrome.py` | 📚 LIBRARY | canonical palindrome check |
| `is_rotated.py` | 🧩 EXAMPLE | leetcode |
| `judge_circle.py` | 🧩 EXAMPLE | leetcode |
| `knuth_morris_pratt.py` | 📚 LIBRARY | KMP |
| `license_number.py` | 🧩 EXAMPLE | leetcode |
| `longest_common_prefix.py` | 🧩 EXAMPLE | leetcode |
| `longest_palindromic_substring.py` | ❓ AMBIGUOUS | leetcode-origin but canonical DP/expand-around-center problem |
| `make_sentence.py` | 🧩 EXAMPLE | trie-based segmentation, leetcode-flavored |
| `manacher.py` | 📚 LIBRARY | Manacher's algorithm |
| `merge_string_checker.py` | 🧩 EXAMPLE | leetcode |
| `min_distance.py` | 🧩 EXAMPLE | leetcode |
| `multiply_strings.py` | 🧩 EXAMPLE | leetcode |
| `one_edit_distance.py` | 🧩 EXAMPLE | leetcode |
| `panagram.py` | 🧩 EXAMPLE | leetcode (typo: should be "pangram"; duplicate of check_pangram) |
| `rabin_karp.py` | 📚 LIBRARY | Rabin-Karp |
| `repeat_string.py` | 🧩 EXAMPLE | leetcode |
| `repeat_substring.py` | 🧩 EXAMPLE | leetcode |
| `reverse_string.py` | 📚 LIBRARY | canonical |
| `reverse_vowel.py` | 🧩 EXAMPLE | leetcode |
| `reverse_words.py` | 🧩 EXAMPLE | leetcode |
| `roman_to_int.py` | 📚 LIBRARY | canonical roman-numeral parse |
| `rotate.py` | 🧩 EXAMPLE | leetcode |
| `strip_url_params.py` | 🧩 EXAMPLE | utility puzzle |
| `strong_password.py` | 🧩 EXAMPLE | leetcode |
| `swap_characters.py` | 🧩 EXAMPLE | leetcode |
| `text_justification.py` | 🧩 EXAMPLE | leetcode (greedy variant — Knuth's DP variant would be library) |
| `unique_morse.py` | 🧩 EXAMPLE | leetcode |
| `validate_coordinates.py` | 🧩 EXAMPLE | leetcode |
| `word_squares.py` | 🧩 EXAMPLE | leetcode (trie + backtrack) |
| `z_algorithm.py` | 📚 LIBRARY | Z-algorithm |

⚠️ Note: `panagram.py` and `check_pangram.py` are likely duplicates with
a typo in one name. Worth consolidating during the move.

## tree/

| File | Bucket | Reason |
|---|---|---|
| `bin_tree_to_list.py` | 🧩 EXAMPLE | leetcode "flatten BT to LL" |
| `binary_tree_paths.py` | 🧩 EXAMPLE | leetcode |
| `binary_tree_views.py` | 🧩 EXAMPLE | leetcode (left/right/top/bottom views) |
| `bst_array_to_bst.py` | 📚 LIBRARY | canonical sorted-array → BST |
| `bst_closest_value.py` | 🧩 EXAMPLE | leetcode |
| `bst_count_left_node.py` | 🧩 EXAMPLE | specific |
| `bst_delete_node.py` | 📚 LIBRARY | canonical BST delete |
| `bst_depth_sum.py` | 🧩 EXAMPLE | specific |
| `bst_height.py` | 📚 LIBRARY | canonical BST height |
| `bst_is_bst.py` | 📚 LIBRARY | canonical BST validation |
| `bst_iterator.py` | 🧩 EXAMPLE | leetcode "BST iterator" |
| `bst_kth_smallest.py` | 📚 LIBRARY | canonical kth-smallest via inorder |
| `bst_lowest_common_ancestor.py` | 📚 LIBRARY | canonical BST-LCA |
| `bst_num_empty.py` | 🧩 EXAMPLE | specific |
| `bst_predecessor.py` | 📚 LIBRARY | canonical in-order predecessor |
| `bst_serialize_deserialize.py` | 🧩 EXAMPLE | leetcode |
| `bst_successor.py` | 📚 LIBRARY | canonical in-order successor |
| `bst_unique_bst.py` | 🧩 EXAMPLE | leetcode "unique BSTs" (Catalan numbers) |
| `bst_validate_bst.py` | 📚 LIBRARY | duplicate of `bst_is_bst`? — verify and merge |
| `construct_tree_postorder_preorder.py` | 📚 LIBRARY | canonical tree reconstruction |
| `deepest_left.py` | 🧩 EXAMPLE | specific |
| `invert_tree.py` | 🧩 EXAMPLE | leetcode (the famous Homebrew interview) |
| `is_balanced.py` | 🧩 EXAMPLE | leetcode |
| `is_subtree.py` | 🧩 EXAMPLE | leetcode |
| `is_symmetric.py` | 🧩 EXAMPLE | leetcode |
| `longest_consecutive.py` | 🧩 EXAMPLE | leetcode |
| `lowest_common_ancestor.py` | 📚 LIBRARY | canonical general-tree LCA |
| `max_height.py` | 🧩 EXAMPLE | leetcode |
| `max_path_sum.py` | 🧩 EXAMPLE | leetcode |
| `min_height.py` | 🧩 EXAMPLE | leetcode |
| `path_sum.py` | 🧩 EXAMPLE | leetcode |
| `path_sum2.py` | 🧩 EXAMPLE | leetcode |
| `pretty_print.py` | ❓ AMBIGUOUS | utility but feels library-ish; keep with TreeNode? |
| `same_tree.py` | 🧩 EXAMPLE | leetcode |
| `traversal_inorder.py` | 📚 LIBRARY | canonical |
| `traversal_level_order.py` | 📚 LIBRARY | canonical |
| `traversal_postorder.py` | 📚 LIBRARY | canonical |
| `traversal_preorder.py` | 📚 LIBRARY | canonical |
| `traversal_zigzag.py` | 🧩 EXAMPLE | leetcode |
| `tree.py` | 📚 LIBRARY | TreeNode (also in `common/`) |
| `trie_add_and_search.py` | 🧩 EXAMPLE | leetcode "implement trie" (the real trie is in `data_structures/`) |

⚠️ Note: `bst_validate_bst.py` and `bst_is_bst.py` need a duplicate check.
Same with `tree/tree.py` vs `common/tree_node.py`.

---

## Cross-cutting issues surfaced during triage

These don't fit a per-category bucket but should be resolved as part of
the migration:

1. **Duplicate name, different impl**: `array/two_sum.py` vs
   `searching/two_sum.py`. Likely should consolidate or rename one.
2. **Possible literal duplicates**: `map/randomized_set.py` vs
   `set/randomized_set.py`; `tree/bst_validate_bst.py` vs
   `tree/bst_is_bst.py`; `tree/tree.py` vs `common/tree_node.py`;
   `string/panagram.py` vs `string/check_pangram.py`.
3. **Misfiled**: `backtracking/anagram.py` doesn't backtrack;
   `graph/all_factors.py` isn't graph-related;
   `tree/trie_add_and_search.py` is leetcode (real trie lives in `data_structures/`).
4. **Conceptual duplicates**: `dynamic_programming/longest_common_subsequence.py`
   vs `map/longest_common_substring.py` — different algorithms (after the
   recent rename) but worth cross-linking in docs.

## Open questions for you

1. **The 9 ambiguous calls** — do you want to settle these now, file-by-file,
   or just give me a default ("when in doubt, library" / "when in doubt,
   example") and I'll apply it across the board?
2. **`linked_list/` philosophy** — I split it operation-by-operation (e.g.
   `reverse.py` = library, `add_two_numbers.py` = example). Alternative: put
   the whole folder into library and move only the obvious leetcode ones to
   examples. Your call.
3. **Sub-categories under `examples/`** — flat `examples/*.py` (320+ files
   in one folder, hard to browse) vs `examples/<topic>/*.py` mirroring the
   current category layout? Recommend the latter.
4. **Tests** — do test files follow the move? I.e., should
   `tests/test_array.py` split into `tests/test_array.py` (library only)
   and `examples/tests/test_array.py`, or keep one test file per category
   that imports from both?
