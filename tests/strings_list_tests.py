import math
import pytest
from problems import strings_list as SL


def test_sl_01_count_vowels():
    assert SL.sl_01_count_vowels("University of Chicago") == 8
    assert SL.sl_01_count_vowels("") == 0
    assert SL.sl_01_count_vowels("bcd fgh") == 0
    assert SL.sl_01_count_vowels("AEIOUaeiou") == 10
    assert SL.sl_01_count_vowels("PyThOn") == 1

def test_sl_02_count_substring_overlapping():
    assert SL.sl_02_count_substring_overlapping("aaaa", "aa") == 3
    assert SL.sl_02_count_substring_overlapping("abc", "d") == 0
    assert SL.sl_02_count_substring_overlapping("abababa", "aba") == 3
    assert SL.sl_02_count_substring_overlapping("xxxxx", "xx") == 4
    assert SL.sl_02_count_substring_overlapping("mississippi", "issi") == 2

def test_sl_03_first_unique_char_index():
    assert SL.sl_03_first_unique_char_index("leetcode") == 0
    assert SL.sl_03_first_unique_char_index("aabb") == -1
    assert SL.sl_03_first_unique_char_index("aabccdeeff") == 2
    assert SL.sl_03_first_unique_char_index("") == -1
    assert SL.sl_03_first_unique_char_index("xxyzx") == 2

def test_sl_04_reverse_words():
    assert SL.sl_04_reverse_words("the sky is blue") == "blue is sky the"
    assert SL.sl_04_reverse_words("hello") == "hello"
    assert SL.sl_04_reverse_words("  a   b  c  ") == "c b a"
    assert SL.sl_04_reverse_words("foo bar") == "bar foo"
    assert SL.sl_04_reverse_words("") == ""

def test_sl_05_is_palindrome_alnum_casefold():
    assert SL.sl_05_is_palindrome_alnum_casefold("Madam, I'm Adam") is True
    assert SL.sl_05_is_palindrome_alnum_casefold("Chicago") is False
    assert SL.sl_05_is_palindrome_alnum_casefold("A man, a plan, a canal: Panama") is True
    assert SL.sl_05_is_palindrome_alnum_casefold("") is True
    assert SL.sl_05_is_palindrome_alnum_casefold("No 'x' in Nixon") is True

def test_sl_06_run_length_encode():
    assert SL.sl_06_run_length_encode("aaabbc") == "a3b2c1"
    assert SL.sl_06_run_length_encode("") == ""
    assert SL.sl_06_run_length_encode("a") == "a1"
    assert SL.sl_06_run_length_encode("abba") == "a1b2a1"
    assert SL.sl_06_run_length_encode("xxxxxxy") == "x6y1"

def test_sl_07_compress_spaces():
    assert SL.sl_07_compress_spaces("  a   b  c  ") == "a b c"
    assert SL.sl_07_compress_spaces("") == ""
    assert SL.sl_07_compress_spaces("hello") == "hello"
    assert SL.sl_07_compress_spaces("  multiple\t\tspaces\nhere ") == "multiple spaces here"
    assert SL.sl_07_compress_spaces(" a  b   ") == "a b"

def test_sl_08_longest_common_prefix():
    assert SL.sl_08_longest_common_prefix(["flower","flow","flight"]) == "fl"
    assert SL.sl_08_longest_common_prefix(["dog","racecar","car"]) == ""
    assert SL.sl_08_longest_common_prefix([]) == ""
    assert SL.sl_08_longest_common_prefix(["in","inch","inn"]) == "in"
    assert SL.sl_08_longest_common_prefix(["a"]) == "a"

def test_sl_09_rotate_right():
    assert SL.sl_09_rotate_right([1,2,3,4,5], 2) == [4,5,1,2,3]
    assert SL.sl_09_rotate_right([], 5) == []
    assert SL.sl_09_rotate_right([1,2,3], 0) == [1,2,3]
    assert SL.sl_09_rotate_right([1,2,3], -1) == [1,2,3]
    assert SL.sl_09_rotate_right([1], 10) == [1]

def test_sl_10_dedupe_preserve_order():
    assert SL.sl_10_dedupe_preserve_order([1,2,1,3,2,4]) == [1,2,3,4]
    assert SL.sl_10_dedupe_preserve_order([]) == []
    assert SL.sl_10_dedupe_preserve_order([1,1,1]) == [1]
    assert SL.sl_10_dedupe_preserve_order(["a","b","a","c"]) == ["a","b","c"]
    assert SL.sl_10_dedupe_preserve_order([3,2,3,2,1]) == [3,2,1]

def test_sl_11_flatten_once():
    assert SL.sl_11_flatten_once([[1,2],[3],[4,5]]) == [1,2,3,4,5]
    assert SL.sl_11_flatten_once([]) == []
    assert SL.sl_11_flatten_once([[1],[]]) == [1]
    assert SL.sl_11_flatten_once([["a","b"],["c"]]) == ["a","b","c"]
    assert SL.sl_11_flatten_once([[1,2,3]]) == [1,2,3]

def test_sl_12_pairwise_sum():
    assert SL.sl_12_pairwise_sum([1,2,3],[10,20]) == [11,22]
    assert SL.sl_12_pairwise_sum([], [1,2]) == []
    assert SL.sl_12_pairwise_sum([5],[7,9]) == [12]
    assert SL.sl_12_pairwise_sum([0,0],[0,0,0]) == [0,0]
    assert SL.sl_12_pairwise_sum([2,4,6],[1,3,5]) == [3,7,11]

def test_sl_13_window_sums():
    assert SL.sl_13_window_sums([1,2,3,4,5], 3) == [6,9,12]
    assert SL.sl_13_window_sums([1,2], 3) == []
    assert SL.sl_13_window_sums([5,5,5,5], 2) == [10,10,10]
    assert SL.sl_13_window_sums([], 1) == []
    assert SL.sl_13_window_sums([1,2,3], 1) == [1,2,3]

def test_sl_14_mode_smallest_on_tie():
    assert SL.sl_14_mode_smallest_on_tie([1,1,2,2,3]) == 1
    assert SL.sl_14_mode_smallest_on_tie([]) is None
    assert SL.sl_14_mode_smallest_on_tie([4]) == 4
    assert SL.sl_14_mode_smallest_on_tie([3,3,2,2,1,1]) == 1
    assert SL.sl_14_mode_smallest_on_tie([2,2,2,1,1]) == 2

def test_sl_15_unique_sorted():
    assert SL.sl_15_unique_sorted([3,1,2,1,3]) == [1,2,3]
    assert SL.sl_15_unique_sorted([]) == []
    assert SL.sl_15_unique_sorted([5,5,5]) == [5]
    assert SL.sl_15_unique_sorted([2,1,2,1]) == [1,2]
    assert SL.sl_15_unique_sorted([10,9,8,9]) == [8,9,10]

def test_sl_16_list_median():
    assert SL.sl_16_list_median([3,1,2]) == 2
    assert SL.sl_16_list_median([1,2,3,4]) == 2.5
    assert SL.sl_16_list_median([]) is None
    assert SL.sl_16_list_median([7]) == 7
    assert SL.sl_16_list_median([1,1,1,1]) == 1.0

def test_sl_17_interleave_zip_longest():
    assert SL.sl_17_interleave_zip_longest([1,2,3],["a","b"]) == [1,"a",2,"b",3,None]
    assert SL.sl_17_interleave_zip_longest([1], [2,3,4], fill=0) == [1,2,0,3,0,4]
    assert SL.sl_17_interleave_zip_longest([], [1,2]) == [None,1,None,2]
    assert SL.sl_17_interleave_zip_longest([1,2], []) == [1,None,2,None]
    assert SL.sl_17_interleave_zip_longest([], []) == []

def test_sl_18_two_sum_indices():
    assert SL.sl_18_two_sum_indices([2,7,11,15], 9) == (0,1)
    assert SL.sl_18_two_sum_indices([1,2,3], 7) is None
    assert SL.sl_18_two_sum_indices([3,2,4], 6) in {(1,2),(0,2),(0,1)}
    assert SL.sl_18_two_sum_indices([], 0) is None
    assert SL.sl_18_two_sum_indices([0,4,3,0], 0) in {(0,3),(3,0)}

def test_sl_19_word_frequencies():
    assert SL.sl_19_word_frequencies("To be, or not to be?") == [('be',2),('to',2),('not',1),('or',1)]
    assert SL.sl_19_word_frequencies("") == []
    assert SL.sl_19_word_frequencies("a A a") == [('a',3)]
    assert SL.sl_19_word_frequencies("x y x z") == [('x',2),('y',1),('z',1)]
    assert SL.sl_19_word_frequencies("...") == []

def test_sl_20_top_k_words():
    assert SL.sl_20_top_k_words("a a b b b C c", 3) == ['b','a','c']
    assert SL.sl_20_top_k_words("", 5) == []
    assert SL.sl_20_top_k_words("one two two three three three", 2) == ['three','two']
    assert SL.sl_20_top_k_words("tie Tie tIe z", 1) == ['tie']
    assert SL.sl_20_top_k_words("x y z", 0) == []

def test_sl_21_caesar_shift():
    assert SL.sl_21_caesar_shift("Abc-Z", 2) == "Cde-B"
    assert SL.sl_21_caesar_shift("Hello, World!", 13) == "Uryyb, Jbeyq!"
    assert SL.sl_21_caesar_shift("xyz", 3) == "abc"
    assert SL.sl_21_caesar_shift("ABC", -1) == "ZAB"
    assert SL.sl_21_caesar_shift("no-change 123", 0) == "no-change 123"

def test_sl_22_is_anagram():
    assert SL.sl_22_is_anagram("Dormitory", "Dirty room!!") is True
    assert SL.sl_22_is_anagram("abc", "abz") is False
    assert SL.sl_22_is_anagram("A gentleman", "Elegant man") is True
    assert SL.sl_22_is_anagram("", "") is True
    assert SL.sl_22_is_anagram("rat", "car") is False

def test_sl_23_longest_run_char():
    assert SL.sl_23_longest_run_char("aaabbccccd") == ('c',4)
    assert SL.sl_23_longest_run_char("") == (None,0)
    assert SL.sl_23_longest_run_char("a") == ('a',1)
    assert SL.sl_23_longest_run_char("bbbaa") == ('b',3)
    assert SL.sl_23_longest_run_char("abbbbcc") == ('b',4)

def test_sl_24_longest_palindromic_substring():
    assert SL.sl_24_longest_palindromic_substring("babad") in ("bab","aba")
    assert SL.sl_24_longest_palindromic_substring("cbbd") == "bb"
    assert SL.sl_24_longest_palindromic_substring("") == ""
    assert SL.sl_24_longest_palindromic_substring("a") == "a"
    assert SL.sl_24_longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_sl_25_most_frequent_char():
    assert SL.sl_25_most_frequent_char("abbbbccddeee") == "b"
    assert SL.sl_25_most_frequent_char("") is None
    assert SL.sl_25_most_frequent_char("aabb") == "a"
    assert SL.sl_25_most_frequent_char("xyz") == "x"
    assert SL.sl_25_most_frequent_char("zzzaaa") == "a"

def test_sl_26_remove_adjacent_k_duplicates():
    assert SL.sl_26_remove_adjacent_k_duplicates("deeedbbcccbdaa", 3) == "aa"
    assert SL.sl_26_remove_adjacent_k_duplicates("pbbcggttciiippooaais", 2) == "ps"
    assert SL.sl_26_remove_adjacent_k_duplicates("", 2) == ""
    assert SL.sl_26_remove_adjacent_k_duplicates("aaa", 3) == ""
    assert SL.sl_26_remove_adjacent_k_duplicates("abba", 2) == ""

def test_sl_27_common_characters():
    assert SL.sl_27_common_characters("abc", "bcd") == ["b","c"]
    assert SL.sl_27_common_characters("", "xyz") == []
    assert SL.sl_27_common_characters("aA", "Aa") == ["A","a"] if "A" in "Aa" else ["a"]  # case sensitive
    assert SL.sl_27_common_characters("hello", "world") == ["l","o"]
    assert SL.sl_27_common_characters("abc", "DEF") == []

def test_sl_28_group_anagrams():
    assert SL.sl_28_group_anagrams(["eat","Tea","tan","ate","Nat","bat"]) == [['eat','Tea','ate'],['tan','Nat'],['bat']]
    assert SL.sl_28_group_anagrams([]) == []
    assert SL.sl_28_group_anagrams(["a"]) == [["a"]]
    assert SL.sl_28_group_anagrams(["ab","ba","AB"]) == [["ab","ba","AB"]]
    assert SL.sl_28_group_anagrams(["x","y","x"]) == [["x","x"],["y"]]

def test_sl_29_reverse_each_word():
    assert SL.sl_29_reverse_each_word("ab cd ef") == "ba dc fe"
    assert SL.sl_29_reverse_each_word("hello") == "olleh"
    assert SL.sl_29_reverse_each_word("") == ""
    assert SL.sl_29_reverse_each_word("a b") == "a b"
    assert SL.sl_29_reverse_each_word("Python 3") == "nohtyP 3"

def test_sl_30_kth_non_overlapping():
    assert SL.sl_30_kth_non_overlapping("aaaaaa", "aa", 3) == 4
    assert SL.sl_30_kth_non_overlapping("abc", "x", 1) == -1
    assert SL.sl_30_kth_non_overlapping("ababab", "ab", 2) == 2
    assert SL.sl_30_kth_non_overlapping("aaa", "a", 2) == 1
    assert SL.sl_30_kth_non_overlapping("", "a", 1) == -1

def test_sl_31_strip_outer_parentheses():
    assert SL.sl_31_strip_outer_parentheses("(a+(b*c))") == "a+(b*c)"
    assert SL.sl_31_strip_outer_parentheses("a+(b*c)") == "a+(b*c)"
    assert SL.sl_31_strip_outer_parentheses("((x))") == "(x)"
    assert SL.sl_31_strip_outer_parentheses("") == ""
    assert SL.sl_31_strip_outer_parentheses("(x)+y") == "(x)+y"

def test_sl_35_partition_by_parity():
    assert SL.sl_35_partition_by_parity([3,2,4,1,5]) == [2,4,3,1,5]
    assert SL.sl_35_partition_by_parity([]) == []
    assert SL.sl_35_partition_by_parity([2,4,6]) == [2,4,6]
    assert SL.sl_35_partition_by_parity([1,3,5]) == [1,3,5]
    assert SL.sl_35_partition_by_parity([0,1,2]) == [0,2,1]

def test_sl_36_max_subarray_sum():
    assert SL.sl_36_max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert SL.sl_36_max_subarray_sum([]) == 0
    assert SL.sl_36_max_subarray_sum([1]) == 1
    assert SL.sl_36_max_subarray_sum([-1,-2,-3]) == -1
    assert SL.sl_36_max_subarray_sum([5,-2,3]) == 6

def test_sl_37_longest_increasing_run():
    assert SL.sl_37_longest_increasing_run([1,2,2,3,4,1]) == 3
    assert SL.sl_37_longest_increasing_run([]) == 0
    assert SL.sl_37_longest_increasing_run([1]) == 1
    assert SL.sl_37_longest_increasing_run([5,4,3,2]) == 1
    assert SL.sl_37_longest_increasing_run([1,2,3,4,5]) == 5

def test_sl_38_chunk():
    assert SL.sl_38_chunk([1,2,3,4,5], 2) == [[1,2],[3,4],[5]]
    assert SL.sl_38_chunk([], 3) == []
    assert SL.sl_38_chunk([1,2,3], 1) == [[1],[2],[3]]
    assert SL.sl_38_chunk([1,2,3,4], 3) == [[1,2,3],[4]]
    assert SL.sl_38_chunk([1], 10) == [[1]]

def test_sl_39_transpose():
    assert SL.sl_39_transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]
    assert SL.sl_39_transpose([]) == []
    assert SL.sl_39_transpose([[1]]) == [[1]]
    assert SL.sl_39_transpose([[1,2]]) == [[1],[2]]
    assert SL.sl_39_transpose([[1],[2]]) == [[1,2]]

def test_sl_40_diagonal_sums():
    assert SL.sl_40_diagonal_sums([[1,2],[3,4]]) == (5,5)
    assert SL.sl_40_diagonal_sums([]) == (0,0)
    assert SL.sl_40_diagonal_sums([[7]]) == (7,7)
    assert SL.sl_40_diagonal_sums([[1,0,2],[0,3,0],[4,0,5]]) == (9,9)
    assert SL.sl_40_diagonal_sums([[2,3,4],[5,6,7],[8,9,1]]) == (9,18)

def test_sl_41_rotate_matrix_90_cw():
    assert SL.sl_41_rotate_matrix_90_cw([[1,2,3],[4,5,6]]) == [[4,1],[5,2],[6,3]]
    assert SL.sl_41_rotate_matrix_90_cw([]) == []
    assert SL.sl_41_rotate_matrix_90_cw([[1]]) == [[1]]
    assert SL.sl_41_rotate_matrix_90_cw([[1,2],[3,4],[5,6]]) == [[5,3,1],[6,4,2]]
    assert SL.sl_41_rotate_matrix_90_cw([[0,1],[2,3]]) == [[2,0],[3,1]]

def test_sl_42_merge_sorted():
    assert SL.sl_42_merge_sorted([1,3,5],[2,4,6]) == [1,2,3,4,5,6]
    assert SL.sl_42_merge_sorted([],[]) == []
    assert SL.sl_42_merge_sorted([1],[2]) == [1,2]
    assert SL.sl_42_merge_sorted([1,1,2],[1,2,2]) == [1,1,1,2,2,2]
    assert SL.sl_42_merge_sorted([], [1,2]) == [1,2]

def test_sl_43_insertion_index():
    assert SL.sl_43_insertion_index([1,2,4,4,5], 4) == 2
    assert SL.sl_43_insertion_index([], 7) == 0
    assert SL.sl_43_insertion_index([1,3,5], 0) == 0
    assert SL.sl_43_insertion_index([1,3,5], 6) == 3
    assert SL.sl_43_insertion_index([1,1,1], 1) == 0

def test_sl_44_stable_unique_by_key():
    assert SL.sl_44_stable_unique_by_key([[1,'a'],[2,'b'],[1,'x'],[3,'b']], 0) == [[1,'a'],[2,'b'],[3,'b']]
    assert SL.sl_44_stable_unique_by_key([], 0) == []
    assert SL.sl_44_stable_unique_by_key([[1,'a']], 0) == [[1,'a']]
    assert SL.sl_44_stable_unique_by_key([[1,'a'],[2,'a'],[3,'a']], 1) == [[1,'a']]
    assert SL.sl_44_stable_unique_by_key([[1,1],[2,1],[3,2],[4,2]], 1) == [[1,1],[3,2]]

def test_sl_45_frequency_table():
    assert SL.sl_45_frequency_table([3,1,2,1,3,3]) == [(3,3),(1,2),(2,1)]
    assert SL.sl_45_frequency_table([]) == []
    assert SL.sl_45_frequency_table(["a","b","a"]) == [("a",2),("b",1)]
    assert SL.sl_45_frequency_table([1,1,2,2]) == [(1,2),(2,2)]
    assert SL.sl_45_frequency_table([2]) == [(2,1)]

def test_sl_46_majority_element():
    assert SL.sl_46_majority_element([2,2,1,2,3,2,2]) == 2
    assert SL.sl_46_majority_element([1,2,3]) is None
    assert SL.sl_46_majority_element([]) is None
    assert SL.sl_46_majority_element([1,1,1]) == 1
    assert SL.sl_46_majority_element([3,3,4]) == 3

def test_sl_47_two_sum_all_pairs():
    assert SL.sl_47_two_sum_all_pairs([1,2,3,4,3], 6) == [(1,3),(2,4)]
    assert SL.sl_47_two_sum_all_pairs([], 10) == []
    assert SL.sl_47_two_sum_all_pairs([0,0,0], 0) == [(0,1),(0,2),(1,2)]
    assert SL.sl_47_two_sum_all_pairs([1,5,1,5], 6) == [(0,1),(0,3),(1,2),(2,3)]
    assert SL.sl_47_two_sum_all_pairs([2,2,2,2], 4) == [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def test_sl_48_sliding_window_max():
    assert SL.sl_48_sliding_window_max([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert SL.sl_48_sliding_window_max([2,1], 3) == []
    assert SL.sl_48_sliding_window_max([9,8,7], 1) == [9,8,7]
    assert SL.sl_48_sliding_window_max([], 2) == []
    assert SL.sl_48_sliding_window_max([1,2,3,4], 2) == [2,3,4]

def test_sl_49_matrix_is_magic_square():
    assert SL.sl_49_matrix_is_magic_square([[8,1,6],[3,5,7],[4,9,2]]) is True
    assert SL.sl_49_matrix_is_magic_square([[1,2],[3,4]]) is False
    assert SL.sl_49_matrix_is_magic_square([]) is False
    assert SL.sl_49_matrix_is_magic_square([[2]]) is False
    assert SL.sl_49_matrix_is_magic_square([[4,9,2],[3,5,7],[8,1,6]]) is True

def test_sl_32_word_wrap():
    assert SL.sl_32_word_wrap("a bb ccc dddd", 5) == ["a bb","ccc","dddd"]
    assert SL.sl_32_word_wrap("", 10) == []
    assert SL.sl_32_word_wrap("one two three four", 7) == ["one two","three","four"]
    assert SL.sl_32_word_wrap("  many   spaces  here ", 6) == ["many","spaces","here"]
    assert SL.sl_32_word_wrap("word", 10) == ["word"]

def test_sl_33_ngram_counts():
    assert SL.sl_33_ngram_counts("ABAB!", 2) == [("ab",2),("ba",1)]
    assert SL.sl_33_ngram_counts("", 3) == []
    assert SL.sl_33_ngram_counts("aaaa", 2) == [("aa",3)]
    assert SL.sl_33_ngram_counts("a-b_c", 1) == [("a",1),("b",1),("c",1)]
    assert SL.sl_33_ngram_counts("XYxy", 2) == [("xy",2),("yx",1)]

def test_sl_34_top_k_bigrams():
    assert SL.sl_34_top_k_bigrams("to be or not to be", 2) == [(("to","be"),2),(("be","or"),1)]
    assert SL.sl_34_top_k_bigrams("", 5) == []
    assert SL.sl_34_top_k_bigrams("a a a a", 3) == [(("a","a"),3)]
    assert SL.sl_34_top_k_bigrams("x y z", 10) == [(("x","y"),1),(("y","z"),1)]
    assert SL.sl_34_top_k_bigrams("Repeat repeat REPEAT", 1) == [(("repeat","repeat"),2)]

def test_sl_50_longest_common_suffix():
    assert SL.sl_50_longest_common_suffix(["running","jogging","ping"]) == "ing"
    assert SL.sl_50_longest_common_suffix(["abc","def"]) == ""
    assert SL.sl_50_longest_common_suffix([]) == ""
    assert SL.sl_50_longest_common_suffix(["a"]) == "a"
    assert SL.sl_50_longest_common_suffix(["testing","ing","bring"]) == "ing"

def test_sl_51_longest_substring_k_distinct():
    assert SL.sl_51_longest_substring_k_distinct("eceba", 2) == 3
    assert SL.sl_51_longest_substring_k_distinct("aa", 1) == 2
    assert SL.sl_51_longest_substring_k_distinct("", 3) == 0
    assert SL.sl_51_longest_substring_k_distinct("abcabcbb", 2) == 4
    assert SL.sl_51_longest_substring_k_distinct("aabbcc", 1) == 2

def test_sl_52_min_window_substring():
    assert SL.sl_52_min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert SL.sl_52_min_window_substring("a", "aa") == ""
    assert SL.sl_52_min_window_substring("a", "a") == "a"
    assert SL.sl_52_min_window_substring("ab", "b") == "b"
    assert SL.sl_52_min_window_substring("ab", "ab") == "ab"

def test_sl_53_remove_min_to_make_valid_parentheses():
    assert SL.sl_53_remove_min_to_make_valid_parentheses("a)b(c)d") == "ab(c)d"
    assert SL.sl_53_remove_min_to_make_valid_parentheses(")a((b)c(") == "a(b)c"
    assert SL.sl_53_remove_min_to_make_valid_parentheses("))((") == ""
    assert SL.sl_53_remove_min_to_make_valid_parentheses("abc") == "abc"
    assert SL.sl_53_remove_min_to_make_valid_parentheses("(a(b)c)d)") == "a(b)c)d" or SL.sl_53_remove_min_to_make_valid_parentheses("(a(b)c)d)") == "(a(b)c)d"

def test_sl_54_smallest_subsequence_distinct():
    assert SL.sl_54_smallest_subsequence_distinct("cbacdcbc") == "acdb"
    assert SL.sl_54_smallest_subsequence_distinct("bcabc") == "abc"
    assert SL.sl_54_smallest_subsequence_distinct("aaaa") == "a"
    assert SL.sl_54_smallest_subsequence_distinct("") == ""
    assert SL.sl_54_smallest_subsequence_distinct("cdadabcc") == "adbc"

def test_sl_55_decode_string_nested():
    assert SL.sl_55_decode_string_nested("3[a]2[bc]") == "aaabcbc"
    assert SL.sl_55_decode_string_nested("3[a2[c]]") == "accaccacc"
    assert SL.sl_55_decode_string_nested("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert SL.sl_55_decode_string_nested("10[z]") == "z"*10
    assert SL.sl_55_decode_string_nested("x") == "x"

def test_sl_56_longest_repeating_char_replacement():
    assert SL.sl_56_longest_repeating_char_replacement("ABAB", 2) == 4
    assert SL.sl_56_longest_repeating_char_replacement("AABABBA", 1) == 4
    assert SL.sl_56_longest_repeating_char_replacement("", 3) == 0
    assert SL.sl_56_longest_repeating_char_replacement("AAAA", 0) == 4
    assert SL.sl_56_longest_repeating_char_replacement("ABAA", 0) == 2

def test_sl_57_trap_rain_water():
    assert SL.sl_57_trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert SL.sl_57_trap_rain_water([]) == 0
    assert SL.sl_57_trap_rain_water([2,0,2]) == 2
    assert SL.sl_57_trap_rain_water([3,0,0,2,0,4]) == 10
    assert SL.sl_57_trap_rain_water([1,2,3]) == 0

def test_sl_58_subarray_sum_equals_k_count():
    assert SL.sl_58_subarray_sum_equals_k_count([1,1,1], 2) == 2
    assert SL.sl_58_subarray_sum_equals_k_count([1,2,3], 3) == 2
    assert SL.sl_58_subarray_sum_equals_k_count([], 0) == 0
    assert SL.sl_58_subarray_sum_equals_k_count([0,0,0], 0) == 6
    assert SL.sl_58_subarray_sum_equals_k_count([1,-1,0], 0) == 3

def test_sl_59_lis_length_nlogn():
    assert SL.sl_59_lis_length_nlogn([10,9,2,5,3,7,101,18]) == 4
    assert SL.sl_59_lis_length_nlogn([]) == 0
    assert SL.sl_59_lis_length_nlogn([1]) == 1
    assert SL.sl_59_lis_length_nlogn([3,2,1]) == 1
    assert SL.sl_59_lis_length_nlogn([0,8,4,12,2]) == 3

def test_sl_60_matrix_spiral_order():
    assert SL.sl_60_matrix_spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert SL.sl_60_matrix_spiral_order([]) == []
    assert SL.sl_60_matrix_spiral_order([[1]]) == [1]
    assert SL.sl_60_matrix_spiral_order([[1,2],[3,4]]) == [1,2,4,3]
    assert SL.sl_60_matrix_spiral_order([[1,2,3],[4,5,6]]) == [1,2,3,6,5,4]