# CtCI 6th Edition — Chapter Map

This file is the source of truth for the `ctci-practice` skill's roadmap generation. Each problem has a slug, title, and difficulty tag. The skill reads this file to build per-user ROADMAP.md files.

## Difficulty tagging
- `easy` — straightforward application of one standard technique (1.1–1.3, 2.1, etc.)
- `medium` — requires combining two techniques or handling non-trivial edge cases (most book problems)
- `hard` — advanced algorithm, significant insight required, or Chapter 17 entries

## Chapter 1 — Arrays and Strings
Topic slug: `arrays_strings`
Main techniques: Hash sets, two pointers, in-place matrix ops, string manipulation, sorting.

- 1.1 `is_unique` | Is Unique | easy
- 1.2 `check_permutation` | Check Permutation | easy
- 1.3 `urlify` | URLify | easy
- 1.4 `palindrome_permutation` | Palindrome Permutation | medium
- 1.5 `one_away` | One Away | medium
- 1.6 `string_compression` | String Compression | medium
- 1.7 `rotate_matrix` | Rotate Matrix | medium
- 1.8 `zero_matrix` | Zero Matrix | medium
- 1.9 `string_rotation` | String Rotation | medium

## Chapter 2 — Linked Lists
Topic slug: `linked_lists`
Main techniques: Runner/two-pointer, recursion, in-place pointer manipulation, Floyd's cycle detection.

- 2.1 `remove_dups` | Remove Dups | easy
- 2.2 `return_kth_to_last` | Return Kth To Last | easy
- 2.3 `delete_middle_node` | Delete Middle Node | easy
- 2.4 `partition` | Partition | medium
- 2.5 `sum_lists` | Sum Lists | medium
- 2.6 `palindrome` | Palindrome | medium
- 2.7 `intersection` | Intersection | hard
- 2.8 `loop_detection` | Loop Detection | hard

## Chapter 3 — Stacks and Queues
Topic slug: `stacks_queues`
Main techniques: Stack/queue design, auxiliary stacks, array-backed structures.

- 3.1 `three_in_one` | Three In One | medium
- 3.2 `stack_min` | Stack Min | easy
- 3.3 `stack_of_plates` | Stack Of Plates | medium
- 3.4 `queue_via_stacks` | Queue Via Stacks | easy
- 3.5 `sort_stack` | Sort Stack | medium
- 3.6 `animal_shelter` | Animal Shelter | medium

## Chapter 4 — Trees and Graphs
Topic slug: `trees_graphs`
Main techniques: BFS, DFS, tree traversals, topological sort, BST properties, recursion.

- 4.1 `route_between_nodes` | Route Between Nodes | easy
- 4.2 `minimal_tree` | Minimal Tree | easy
- 4.3 `list_of_depths` | List Of Depths | easy
- 4.4 `check_balanced` | Check Balanced | medium
- 4.5 `validate_bst` | Validate BST | medium
- 4.6 `successor` | Successor | medium
- 4.7 `build_order` | Build Order | hard
- 4.8 `first_common_ancestor` | First Common Ancestor | medium
- 4.9 `bst_sequences` | BST Sequences | hard
- 4.10 `check_subtree` | Check Subtree | medium
- 4.11 `random_node` | Random Node | hard
- 4.12 `paths_with_sum` | Paths With Sum | hard

## Chapter 5 — Bit Manipulation
Topic slug: `bit_manipulation`
Main techniques: Masking, shifting, XOR tricks, two's complement, bitwise arithmetic.

- 5.1 `insertion` | Insertion | easy
- 5.2 `binary_to_string` | Binary To String | medium
- 5.3 `flip_bit_to_win` | Flip Bit To Win | medium
- 5.4 `next_number` | Next Number | hard
- 5.6 `conversion` | Conversion | easy
- 5.7 `pairwise_swap` | Pairwise Swap | medium
- 5.8 `draw_line` | Draw Line | medium

## Chapter 6 — Math and Logic Puzzles
Topic slug: `math_logic`
Main techniques: Worst-case analysis, information theory, probability, adversarial reasoning.

- 6.5 `egg_drop` | Egg Drop | medium
- 6.7 `the_apocalypse` | The Apocalypse | medium
- 6.10 `test_strips` | Test Strips | hard

## Chapter 7 — Object-Oriented Design
Topic slug: `ood`
Main techniques: Class hierarchies, encapsulation, design patterns, interface design.

- 7.1 `deck_of_cards` | Deck Of Cards | medium
- 7.2 `call_center` | Call Center | medium
- 7.3 `jukebox` | Jukebox | medium
- 7.4 `parking_lot` | Parking Lot | medium
- 7.5 `online_book_reader` | Online Book Reader | medium
- 7.6 `jigsaw` | Jigsaw | medium
- 7.7 `chat_server` | Chat Server | medium
- 7.8 `othello` | Othello | medium
- 7.9 `circular_array` | Circular Array | medium
- 7.10 `minesweeper` | Minesweeper | medium
- 7.11 `file_system` | File System | medium
- 7.12 `hash_table` | Hash Table | medium

## Chapter 8 — Recursion and Dynamic Programming
Topic slug: `recursion_dp`
Main techniques: Memoization, tabulation, backtracking, divide-and-conquer, state space search.

- 8.1 `triple_step` | Triple Step | easy
- 8.2 `robot_in_a_grid` | Robot In A Grid | medium
- 8.3 `magic_index` | Magic Index | medium
- 8.4 `power_set` | Power Set | medium
- 8.5 `recursive_multiply` | Recursive Multiply | medium
- 8.6 `towers_of_hanoi` | Towers Of Hanoi | medium
- 8.7 `permutations_without_dups` | Permutations Without Dups | medium
- 8.8 `permutations_with_dups` | Permutations With Dups | medium
- 8.9 `parens` | Parens | medium
- 8.10 `paint_fill` | Paint Fill | medium
- 8.11 `coins` | Coins | hard
- 8.12 `eight_queens` | Eight Queens | hard
- 8.13 `stack_of_boxes` | Stack Of Boxes | hard
- 8.14 `boolean_evaluation` | Boolean Evaluation | hard

## Chapter 10 — Sorting and Searching
Topic slug: `sorting_searching`
Main techniques: Binary search variants, merge sort, bucket sort, bit vectors, external sorting.

- 10.1 `sorted_merge` | Sorted Merge | easy
- 10.2 `group_anagrams` | Group Anagrams | easy
- 10.3 `search_in_rotated_array` | Search In Rotated Array | medium
- 10.4 `sorted_search_no_size` | Sorted Search No Size | medium
- 10.5 `sparse_search` | Sparse Search | medium
- 10.7 `missing_int` | Missing Int | hard
- 10.8 `find_duplicates` | Find Duplicates | medium
- 10.9 `sorted_matrix_search` | Sorted Matrix Search | hard
- 10.10 `rank_from_stream` | Rank From Stream | hard
- 10.11 `peaks_and_valleys` | Peaks And Valleys | medium

## Chapter 16 — Moderate
Topic slug: `moderate`
Main techniques: Mixed — arithmetic tricks, geometry, simulation, parsing, hash maps.

- 16.1 `number_swapper` | Number Swapper | easy
- 16.2 `word_frequencies` | Word Frequencies | medium
- 16.3 `intersection` | Intersection | hard
- 16.4 `tic_tac_win` | Tic Tac Win | medium
- 16.5 `factorial_zeros` | Factorial Zeros | easy
- 16.6 `smallest_difference` | Smallest Difference | medium
- 16.7 `number_max` | Number Max | medium
- 16.8 `english_int` | English Int | medium
- 16.9 `operations` | Operations | hard
- 16.10 `living_people` | Living People | medium
- 16.11 `diving_board` | Diving Board | easy
- 16.12 `xml_encoding` | XML Encoding | medium
- 16.13 `bisect_squares` | Bisect Squares | medium
- 16.14 `best_line` | Best Line | medium
- 16.15 `master_mind` | Master Mind | medium
- 16.16 `sub_sort` | Sub Sort | medium
- 16.17 `contiguous_sequence` | Contiguous Sequence | medium
- 16.18 `pattern_matcher` | Pattern Matcher | hard
- 16.19 `pond_sizes` | Pond Sizes | medium
- 16.20 `t9` | T9 | medium
- 16.21 `sum_swap` | Sum Swap | medium
- 16.22 `langtons_ant` | Langtons Ant | medium
- 16.23 `rand7_from_rand5` | Rand7 From Rand5 | medium
- 16.24 `pairs_with_sum` | Pairs With Sum | easy
- 16.25 `lru_cache` | LRU Cache | medium
- 16.26 `calculator` | Calculator | hard

## Chapter 17 — Hard
Topic slug: `hard`
Main techniques: Advanced DP, tries, heaps, graph algorithms, bit tricks, reservoir sampling.

- 17.1 `add_without_plus` | Add Without Plus | hard
- 17.2 `shuffle` | Shuffle | hard
- 17.3 `random_set` | Random Set | hard
- 17.4 `missing_number` | Missing Number | hard
- 17.5 `letters_and_numbers` | Letters And Numbers | hard
- 17.6 `count_of_2s` | Count Of 2s | hard
- 17.7 `baby_names` | Baby Names | hard
- 17.8 `circus_tower` | Circus Tower | hard
- 17.9 `kth_multiple` | Kth Multiple | hard
- 17.10 `majority_element` | Majority Element | hard
- 17.11 `word_distance` | Word Distance | hard
- 17.12 `binode` | BiNode | hard
- 17.13 `respace` | ReSpace | hard
- 17.14 `smallest_k` | Smallest K | hard
- 17.15 `longest_word` | Longest Word | hard
- 17.16 `the_masseuse` | The Masseuse | hard
- 17.17 `multi_search` | Multi Search | hard
- 17.18 `shortest_supersequence` | Shortest Supersequence | hard
- 17.19 `missing_two` | Missing Two | hard
- 17.20 `continuous_median` | Continuous Median | hard
- 17.21 `volume_of_histogram` | Volume Of Histogram | hard
- 17.22 `word_transformer` | Word Transformer | hard
- 17.23 `max_black_square` | Max Black Square | hard
- 17.24 `max_submatrix` | Max Submatrix | hard
- 17.25 `word_rectangle` | Word Rectangle | hard
- 17.26 `sparse_similarity` | Sparse Similarity | hard

---
**Last updated:** 2026-04-14 (based on CtCI 6th Edition Java directory snapshot).
**Total problems:** 133
