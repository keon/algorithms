<p align="center"><img src="https://raw.githubusercontent.com/keon/algorithms/master/docs/source/_static/logo/logotype1blue.png"></p>

[English](README.md) | 简体中文 | [Deutsch](README_GE.md) | [日本語](README_JP.md) | [한국어](README_KR.md) | [Português](README_PTBR.md) | [Français](README_FR.md)

[![PyPI version](https://badge.fury.io/py/algorithms.svg)](https://badge.fury.io/py/algorithms)
[![Open Source Helpers](https://www.codetriage.com/keon/algorithms/badges/users.svg)](https://www.codetriage.com/keon/algorithms)
[![Build Status](https://travis-ci.org/keon/algorithms.svg?branch=master)](https://travis-ci.org/keon/algorithms)
[![Coverage Status](https://coveralls.io/repos/github/keon/algorithms/badge.svg?branch=master)](https://coveralls.io/github/keon/algorithms?branch=master)

Python版数据结构和算法
=========================================

python版数据结构和算法实现的简约版小示例  

谢谢关注。有多种方法可以贡献你的代码。[从这里开始吧](https://github.com/keon/algorithms/blob/master/CONTRIBUTING.md)  

[或者可以用不同语言来完成上述算法，期待加入](https://github.com/yunshuipiao/sw-algorithms)：https://github.com/yunshuipiao/sw-algorithms

## 测试

### 单元测试
如下代码可以运行全部测试：  
```

python3 -m unittest discover tests

```

针对特定模块(比如：sort)的测试， 可以使用如下代码：  
```

python3 -m unittest tests.test_sort

```

### 使用pytest
如下代码运行所有测试代码：  
```

python3 -m pytest tests

```

## 安装
如果想在代码中使用算法API， 可按如下步骤进行：
```

pip3 install git+https://github.com/keon/algorithms

```

通过创建python文件(比如：在sort模块使用merge_sort)进行测试：
```

from algorithms.sort import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort(my_list)
    print(my_list)

```

## 卸载
如下代码可卸载该API：

```

pip3 uninstall -y algorithms

```

## 实现列表

- [array:数组](arrays)
    - [delete_nth: 删除第n项](algorithms/arrays/delete_nth.py)
    - [flatten：数组降维](algorithms/arrays/flatten.py)
    - [garage：停车场](algorithms/arrays/garage.py)
    - [josephus_problem: 约瑟夫问题](algorithms/arrays/josephus.py)
    - [max_ones_index](algorithms/arrays/max_ones_index.py)
    - [limit](algorithms/arrays/limit.py)
    - [longest_non_repeat：最长不重复子串](algorithms/arrays/longest_non_repeat.py/)
    - [merge_intervals：合并重叠间隔](algorithms/arrays/merge_intervals.py)
    - [missing_ranges：遗失的范围](algorithms/arrays/missing_ranges.py)
    - [plus_one：加一运算](algorithms/arrays/plus_one.py)
    - [rotate：反转数组](algorithms/arrays/rotate.py)
    - [summarize_ranges：数组范围](algorithms/arrays/summarize_ranges.py)
    - [three_sum：三数和为零](algorithms/arrays/three_sum.py)
    - [trimmean](algorithms/arrays/trimmean.py)
    - [top_1](algorithms/arrays/top_1.py)
    - [two_sum：两数和](algorithms/arrays/two_sum.py)
    - [move_zeros: 0后置问题](algorithms/arrays/move_zeros.py)
- [backtrack：回溯](algorithms/backtrack)
    - [general_solution.md：一般方法](algorithms/backtrack/)
    - [anagram：同字母异序词](algorithms/backtrack/anagram.py)
    - [array_sum_combinations：数组和](algorithms/backtrack/array_sum_combinations.py)
    - [combination_sum：和的合并](algorithms/backtrack/combination_sum.py)
    - [expression_add_operators：给表达式添加运算符](algorithms/backtrack/expression_add_operators.py)
    - [factor_combinations：因素组合](algorithms/backtrack/factor_combinations.py)
    - [generate_abbreviations：缩写生成](algorithms/backtrack/generate_abbreviations.py)
    - [generate_parenthesis：括号生成](algorithms/backtrack/generate_parenthesis.py)
    - [letter_combination：字母组合](algorithms/backtrack/letter_combination.py)
    - [palindrome_partitioning：字符串的所有回文子串](algorithms/backtrack/palindrome_partitioning.py)
    - [pattern_match：模式匹配](algorithms/backtrack/pattern_match.py)
    - [permute：排列](algorithms/backtrack/permute.py)
    - [permute_unique：唯一排列](algorithms/backtrack/permute_unique.py)
    - [subsets：子集](algorithms/backtrack/subsets.py)
    - [subsets_unique：唯一子集](algorithms/backtrack/subsets_unique.py)
- [bfs：广度优先搜索](algorithms/bfs)
    - [maze_search](algorithms/bfs/maze_search.py)
    - [shortest_distance_from_all_buildings：所有建筑物的最短路径：](algorithms/bfs/shortest_distance_from_all_buildings.py)
    - [word_ladder：词语阶梯](algorithms/bfs/word_ladder.py)
- [bit：位操作](algorithms/bit)
    - [bytes_int_conversion：字节整数转换](algorithms/bit/bytes_int_conversion.py)
    - [count_ones：统计1出现的次数](algorithms/bit/count_ones.py)
    - [count_flips_to_convert](algorithms/bit/count_flips_to_convert.py)
    - [find_missing_number：寻找缺失数](algorithms/bit/find_missing_number.py)
    - [flip_bit_longest_sequence](algorithms/bit/flip_bit_longest_sequence.py)
    - [power_of_two：2的n次方数判断](algorithms/bit/power_of_two.py)
    - [reverse_bits：反转位](algorithms/bit/reverse_bits.py)
    - [single_number2：寻找出现1次的数（2)](algorithms/bit/single_number2.py)
    - [single_number:寻找出现1次的数（1)](algorithms/bit/single_number.py)
    - [subsets: 求所有子集](algorithms/bit/subsets.py)
    - [add_bitwise_operator：无操作符的加法](algorithms/bit/add_bitwise_operator.py)
- [calculator：计算](algorithms/calculator)
    - [math_parser: 数字解析](algorithms/calculator/math_parser.py)
- [dfs：深度优先搜索](algorithms/dfs)
    - [all_factors：因素分解](algorithms/dfs/all_factors.py)
    - [count_islands：岛计数](algorithms/dfs/count_islands.py)
    - [pacific_atlantic：太平洋大西洋](algorithms/dfs/pacific_atlantic.py)
    - [sudoku_solver：数独解法](algorithms/dfs/sudoku_solver.py)
    - [walls_and_gates：墙和门](algorithms/dfs/walls_and_gates.py)
- [dp：动态规划](algorithms/dp)
    - [buy_sell_stock：股票买卖](algorithms/dp/buy_sell_stock.py)
    - [climbing_stairs：爬梯子问题](algorithms/dp/climbing_stairs.py)
    - [combination_sum：和组合问题](algorithms/dp/combination_sum.py)
    - [house_robber：打家劫舍](algorithms/dp/house_robber.py)
    - [knapsack：背包问题](algorithms/dp/knapsack.py)
    - [longest_increasing：最长递增子序列](algorithms/dp/longest_increasing.py)
    - [max_product_subarray：最大子数组乘积](algorithms/dp/max_product_subarray.py)
    - [max_subarray：最大子数组](algorithms/dp/max_subarray.py)
    - [num_decodings：数字解码](algorithms/dp/num_decodings.py)
    - [regex_matching：正则匹配](algorithms/dp/regex_matching.py)
    - [word_break：单词分割](algorithms/dp/word_break.py)
- [graph：图](graph)
    - [check_bipartite](algorithms/graph/check_bipartite.py)
    - [2-sat：2-sat](algorithms/graph/satisfiability.py)
    - [clone_graph：克隆图](algorithms/graph/clone_graph.py)
    - [cycle_detection：判断圈算法](algorithms/graph/cycle_detection.py)
    - [find_path：发现路径](algorithms/graph/find_path.py)
    - [graph：图](algorithms/graph/graph.py)
    - [traversal：遍历](algorithms/graph/traversal.py)
    - [markov_chain：马尔可夫链](algorithms/graph/markov_chain.py)
- [heap：堆](algorithms/heap)
    - [merge_sorted_k_lists：合并k个有序链](algorithms/heap/merge_sorted_k_lists.py)
    - [skyline：天际线](algorithms/heap/skyline.py)
    - [sliding_window_max：滑动窗口最大值](algorithms/heap/sliding_window_max.py)
- [linkedlist：链表](algorithms/linkedlist)
    - [add_two_numbers：链表数相加](algorithms/linkedlist/add_two_numbers.py)
    - [copy_random_pointer：复制带有随机指针的链表](algorithms/linkedlist/copy_random_pointer.py)
    - [delete_node：删除节点](algorithms/linkedlist/delete_node.py)
    - [first_cyclic_node：环链表的第一个节点](algorithms/linkedlist/first_cyclic_node.py)
    - [is_cyclic：判断环链表](algorithms/linkedlist/is_cyclic.py)
    - [is_palindrome：回文链表](algorithms/linkedlist/is_palindrome.py)
    - [kth_to_last：倒数第k个节点](algorithms/linkedlist/kth_to_last.py)
    - [linkedlist： 链表](algorithms/linkedlist/linkedlist.py)
    - [remove_duplicates：删除重复元素](algorithms/linkedlist/remove_duplicates.py)
    - [reverse：反转链表](algorithms/linkedlist/reverse.py)
    - [rotate_list：旋转链表](algorithms/linkedlist/rotate_list.py)
    - [swap_in_pairs：链表节点交换](algorithms/linkedlist/swap_in_pairs.py)
- [map：映射](algorithms/map)
    - [hashtable：哈希表](algorithms/map/hashtable.py)
    - [separate_chaining_hashtable：拉链法哈希表](algorithms/map/separate_chaining_hashtable.py)
    - [longest_common_subsequence：最长公共子序列](algorithms/map/longest_common_subsequence.py)
    - [randomized_set：随机集](algorithms/map/randomized_set.py)
    - [valid_sudoku：有效数独](algorithms/map/valid_sudoku.py)
- [math：数学问题](algorithms/maths)
    - [extended_gcd：扩展欧几里得算法](algorithms/maths/extended_gcd.py)
    - [combination](algorithms/maths/combination.py)
    - [factorial](algorithms/maths/factorial.py)
    - [gcd/lcm：最大公约数和最小公倍数](algorithms/maths/gcd.py)
    - [prime_test：主要测试](algorithms/maths/prime_test.py)
    - [primes_sieve_of_eratosthenes：埃拉托色尼的质数筛](algorithms/maths/primes_sieve_of_eratosthenes.py)
    - [generate_strobogrammtic：生成对称数](algorithms/maths/generate_strobogrammtic.py)
    - [is_strobogrammatic：判断对称数](algorithms/maths/is_strobogrammatic.py)
    - [modular_exponential](algorithms/maths/modular_exponential.py)
    - [nth_digit：第n位](algorithms/maths/nth_digit.py)
    - [rabin_miller：米勒-拉宾素性检验](algorithms/maths/rabin_miller.py)
    - [rsa：rsa加密](algorithms/maths/rsa.py)
    - [sqrt_precision_factor：开发精度因素](algorithms/maths/sqrt_precision_factor.py)
    - [pythagoras：毕达哥拉斯](algorithms/maths/pythagoras.py)
- [matrix：矩阵](algorithms/matrix)
    - [matrix_rotation：矩阵旋转](algorithms/matrix/matrix_rotation.txt)
    - [copy_transform：复制变换](algorithms/matrix/copy_transform.py)
    - [bomb_enemy：炸弹人](algorithms/matrix/bomb_enemy.py)
    - [rotate_image：旋转图像](algorithms/matrix/rotate_image.py)
    - [sparse_dot_vector：解析点向量](algorithms/matrix/sparse_dot_vector.py)
    - [sparse_mul：稀疏矩阵](algorithms/matrix/sparse_mul.py)
    - [spiral_traversal：循环遍历](algorithms/matrix/spiral_traversal.py)
    - [count_paths：计算路径](algorithms/matrix/count_paths.py)
- [queue：队列](algorithms/queues)
    - [max_sliding_window：最大移动窗口](algorithms/queues/max_sliding_window.py)
    - [moving_average：移动平均](algorithms/queues/moving_average.py)
    - [queue：队列](algorithms/queues/queue.py)
    - [reconstruct_queue：重建队列](algorithms/queues/reconstruct_queue.py)
    - [zigzagiterator：锯齿形迭代](algorithms/queues/zigzagiterator.py)
- [search：查找](algorithms/search)
    - [binary_search：二分查找](algorithms/search/binary_search.py)
    - [count_elem：元素计数](algorithms/search/count_elem.py)
    - [first_occurance：首次出现](algorithms/search/first_occurance.py)
    - [last_occurance：最后一次出现](algorithms/search/last_occurance.py)
    - [linear_search](algorithms/search/linear_search.py)
    - [jump_search](algorithms/search/jump_search.py)
- [set：集合](algorithms/set)
    - [randomized_set：随机集合](algorithms/set/randomized_set.py)
    - [set_covering：集合覆盖](algorithms/set/set_covering.py)
- [sort：排序](algorithms/sort)
    - [bitonic_sort](algorithms/sort/bitonic_sort.py)
    - [bogo_sort](algorithms/sort/bogo_sort.py)
    - [bubble_sort：冒泡排序](algorithms/sort/bubble_sort.py)
    - [bucket_sort](algorithms/sort/bucket_sort.py)
    - [cocktail_shaker_sort](algorithms/sort/cocktail_shaker_sort.py)
    - [comb_sort：梳排序](algorithms/sort/comb_sort.py)
    - [counting_sort：计数排序](algorithms/sort/counting_sort.py)
    - [cycle_sort](algorithms/sort/cycle_sort.py)
    - [gnome_sort](algorithms/sort/gnome_sort.py)
    - [heap_sort：堆排序](algorithms/sort/heap_sort.py)
    - [insertion_sort：插入排序](algorithms/sort/insertion_sort.py)
    - [meeting_rooms：会议室](algorithms/sort/meeting_rooms.py)
    - [merge_sort：归并排序](algorithms/sort/merge_sort.py)
    - [pancake_sort](algorithms/sort/pancake_sort.py)
    - [quick_sort：快速排序](algorithms/sort/quick_sort.py)
    - [radix_sort](algorithms/sort/radix_sort.py)
    - [selection_sort：选择排序](algorithms/sort/selection_sort.py)
    - [shell_sort](algorithms/sort/shell_sort.py)
    - [sort_colors：颜色排序](algorithms/sort/sort_colors.py)
    - [top_sort：top排序](algorithms/sort/top_sort.py)
    - [wiggle_sort：摇摆排序](algorithms/sort/wiggle_sort.py)
- [stack：栈](algorithms/stack)
    - [longest_abs_path：最长相对路径](algorithms/stack/longest_abs_path.py)
    - [simplify_path：简化路径](algorithms/stack/simplify_path.py)
    - [stack：栈](algorithms/stack/stack.py)
    - [valid_parenthesis：验证括号](algorithms/stack/valid_parenthesis.py)
- [string：字符串](algorithms/strings)
    - [add_binary：二进制数相加](algorithms/strings/add_binary.py)
    - [breaking_bad：打破坏](algorithms/strings/breaking_bad.py)
    - [decode_string：字符串编码](algorithms/strings/decode_string.py)
    - [encode_decode：编解码](algorithms/strings/encode_decode.py)
    - [group_anagrams：群组错位词](algorithms/strings/group_anagrams.py)
    - [int_to_roman：整数转换罗马数字](algorithms/strings/int_to_roman.py)
    - [is_palindrome：回文字符串](algorithms/strings/is_palindrome.py)
    - [license_number：拍照号码](algorithms/strings/license_number.py)
    - [make_sentence：造句](algorithms/strings/make_sentence.py)
    - [multiply_strings：字符串相乘](algorithms/strings/multiply_strings.py)
    - [one_edit_distance：一个编辑距离](algorithms/strings/one_edit_distance.py)
    - [rabin_karp：Rabin-Karp 算法](algorithms/strings/rabin_karp.py)
    - [reverse_string：反转字符串](algorithms/strings/reverse_string.py)
    - [reverse_vowel：反转元音](algorithms/strings/reverse_vowel.py)
    - [reverse_words：反转单词](algorithms/strings/reverse_words.py)
    - [roman_to_int：罗马数转换整数](algorithms/strings/roman_to_int.py)
    - [word_squares：单词平方](algorithms/strings/word_squares.py)
- [tree：树](algorithms/tree)
    - [segment-tree：线段树](algorithms/tree/segment_tree)
        - [segment_tree：线段树](algorithms/tree/segment_tree/segment_tree.py)
    - [binary_tree_paths：二叉树路径](algorithms/tree/binary_tree_paths.py)
    - [bintree2list：二叉树转换链表](algorithms/tree/bintree2list.py)
    - [bst：二叉搜索树](algorithms/tree/tree/bst)
        - [array2bst：数组转换](algorithms/tree/bst/array2bst.py)
        - [bst_closest_value：最近二叉搜索树值](algorithms/tree/bst/bst_closest_value.py)
        - [BSTIterator：二叉搜索树迭代](algorithms/tree/bst/BSTIterator.py)
        - [delete_node：删除节点](algorithms/tree/bst/delete_node.py)
        - [is_bst：判断二叉搜索树](algorithms/tree/bst/is_bst.py)
        - [kth_smallest：二叉搜索树的第k小节点](algorithms/tree/bst/kth_smallest.py)
        - [lowest_common_ancestor：最近公共祖先](algorithms/tree/bst/lowest_common_ancestor.py)
        - [predecessor：前任](algorithms/tree/bst/predecessor.py)
        - [serialize_deserialize：序列化反序列化](algorithms/tree/bst/serialize_deserialize.py)
        - [successor：继承者](algorithms/tree/bst/successor.py)
        - [unique_bst：唯一BST](algorithms/tree/bst/unique_bst.py)
    - [deepest_left：最深叶子节点](algorithms/tree/deepest_left.py)
    - [invert_tree：反转树](algorithms/tree/invert_tree.py)
    - [is_balanced：判断平衡树](algorithms/tree/is_balanced.py)
    - [is_subtree：判断子树](algorithms/tree/is_subtree.py)
    - [is_symmetric：判断对称树](algorithms/tree/is_symmetric.py)
    - [longest_consecutive：最长连续节点](algorithms/tree/longest_consecutive.py)
    - [lowest_common_ancestor：最近公共祖先](algorithms/tree/lowest_common_ancestor.py)
    - [max_height：最大高度](algorithms/tree/max_height.py)
    - [max_path_sum：最长路径和](algorithms/tree/max_path_sum.py)
    - [min_height：最小高度](algorithms/tree/min_height.py)
    - [path_sum2：路径和2](algorithms/tree/path_sum2.py)
    - [path_sum：路径和](algorithms/tree/path_sum.py)
    - [pretty_print：完美打印](algorithms/tree/pretty_print.py)
    - [same_tree：相同树](algorithms/tree/same_tree.py)
    - [traversal：遍历](algorithms/tree/traversal)
        - [inorder：中序遍历](algorithms/tree/traversal/inorder.py)
        - [level_order：层次遍历](algorithms/tree/traversal/level_order.py)
        - [postorder](algorithms/tree/traversal/postorder.py)
        - [preorder](algorithms/tree/traversal/preorder.py)
        - [zigzag：锯齿形遍历](algorithms/tree/traversal/zigzag.py)
    - [tree：树](algorithms/tree/tree.py)
    - [trie：字典树](algorithms/tree/trie)
        - [add_and_search：添加和查找](algorithms/tree/trie/add_and_search.py)
        - [trie：字典](algorithms/tree/trie/trie.py)
- [union-find：并查集](algorithms/union-find)
    - [count_islands：岛计数](algorithms/union-find/count_islands.py)


## 贡献
谢谢主要维护人员：

* [Keon Kim](https://github.com/keon)
* [Rahul Goswami](https://github.com/goswami-rahul)
* [Christian Bender](https://github.com/christianbender)
* [Ankit Agarwal](https://github.com/ankit167)
* [Hai Hoang Dang](https://github.com/danghai)
* [Saad](https://github.com/SaadBenn)

以及[所有贡献者](https://github.com/keon/algorithms/graphs/contributors)
