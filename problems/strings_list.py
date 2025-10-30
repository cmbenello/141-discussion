"""
strings_list.py — Strings & Lists Practice Set

Table of Contents
-----------------
# Strings — Basics & Algorithms
- sl_01_count_vowels(s)
- sl_02_count_substring_overlapping(s, sub)
- sl_03_first_unique_char_index(s)
- sl_04_reverse_words(s)
- sl_05_is_palindrome_alnum_casefold(s)
- sl_06_run_length_encode(s)
- sl_07_compress_spaces(s)
- sl_08_longest_common_prefix(strs)
- sl_21_caesar_shift(s, k)
- sl_22_is_anagram(a, b)
- sl_23_longest_run_char(s)
- sl_24_longest_palindromic_substring(s)
- sl_25_most_frequent_char(s)
- sl_26_remove_adjacent_k_duplicates(s, k)
- sl_27_common_characters(a, b)
- sl_28_group_anagrams(words)
- sl_29_reverse_each_word(s)
- sl_30_kth_non_overlapping(s, sub, k)
- sl_31_strip_outer_parentheses(s)

# Lists — Basics & Algorithms
- sl_09_rotate_right(lst, k)
- sl_10_dedupe_preserve_order(lst)
- sl_11_flatten_once(list_of_lists)
- sl_12_pairwise_sum(a, b)
- sl_13_window_sums(lst, k)
- sl_14_mode_smallest_on_tie(lst)
- sl_15_unique_sorted(lst)
- sl_16_list_median(lst)
- sl_17_interleave_zip_longest(a, b, fill)
- sl_18_two_sum_indices(lst, target)
- sl_35_partition_by_parity(lst)
- sl_36_max_subarray_sum(lst)
- sl_37_longest_increasing_run(lst)
- sl_38_chunk(lst, k)
- sl_39_transpose(matrix)
- sl_40_diagonal_sums(matrix)
- sl_41_rotate_matrix_90_cw(matrix)
- sl_42_merge_sorted(a, b)
- sl_43_insertion_index(lst, x)
- sl_44_stable_unique_by_key(rows, key_index)
- sl_45_frequency_table(lst)
- sl_46_majority_element(lst)
- sl_47_two_sum_all_pairs(lst, target)
- sl_48_sliding_window_max(lst, k)
- sl_49_matrix_is_magic_square(matrix)

# Hybrid (Strings ⇄ Lists)
- sl_19_word_frequencies(text)
- sl_20_top_k_words(text, k)
- sl_32_word_wrap(text, width)
- sl_33_ngram_counts(text, n)
- sl_34_top_k_bigrams(text, k)
- sl_50_longest_common_suffix(strs)


# Advanced — Difficulty 4
- sl_51_longest_substring_k_distinct(s, k)
- sl_52_min_window_substring(s, t)
- sl_53_remove_min_to_make_valid_parentheses(s)
- sl_54_smallest_subsequence_distinct(s)
- sl_55_decode_string_nested(s)
- sl_56_longest_repeating_char_replacement(s, k)
- sl_57_trap_rain_water(heights)
- sl_58_subarray_sum_equals_k_count(nums, k)
- sl_59_lis_length_nlogn(lst)
- sl_60_matrix_spiral_order(matrix)
"""

from typing import List, Tuple, Optional, Any, Dict, Set

# -----------------------------
# Strings — Basics & Algorithms
# -----------------------------

def sl_01_count_vowels(s: str) -> int:
    """
    Category: String Basics | Tags: counting, vowels | Difficulty: 1

    Count the number of vowels (a, e, i, o, u) in the string, case-insensitive.

    Args:
        s (str): input string

    Returns:
        int: number of vowels

    Examples:
        >>> sl_01_count_vowels("University of Chicago")
        10
        >>> sl_01_count_vowels("")
        0
    """
    raise ValueError("TODO: implement sl_01_count_vowels")


def sl_02_count_substring_overlapping(s: str, sub: str) -> int:
    """
    Category: String Algorithms | Tags: substring, overlapping | Difficulty: 2

    Count occurrences of `sub` in `s`, allowing overlaps. Empty `sub` is invalid.

    Args:
        s (str): haystack
        sub (str): needle (non-empty)

    Returns:
        int: count of (possibly overlapping) matches

    Examples:
        >>> sl_02_count_substring_overlapping("aaaa", "aa")
        3
        >>> sl_02_count_substring_overlapping("abc", "d")
        0
    """
    raise ValueError("TODO: implement sl_02_count_substring_overlapping")


def sl_03_first_unique_char_index(s: str) -> int:
    """
    Category: String Algorithms | Tags: frequency, indexing | Difficulty: 2

    Return the index of the first character in `s` that appears exactly once; return -1 if none.

    Args:
        s (str): input string

    Returns:
        int: index or -1 if no unique character exists

    Examples:
        >>> sl_03_first_unique_char_index("leetcode")
        0
        >>> sl_03_first_unique_char_index("aabb")
        -1
    """
    raise ValueError("TODO: implement sl_03_first_unique_char_index")


def sl_04_reverse_words(s: str) -> str:
    """
    Category: String Algorithms | Tags: split, join | Difficulty: 1

    Reverse the order of words separated by single spaces. Leading/trailing spaces will be trimmed.

    Args:
        s (str): input

    Returns:
        str: words reversed, single space between words

    Examples:
        >>> sl_04_reverse_words("the sky is blue")
        'blue is sky the'
        >>> sl_04_reverse_words("hello")
        'hello'
    """
    raise ValueError("TODO: implement sl_04_reverse_words")


def sl_05_is_palindrome_alnum_casefold(s: str) -> bool:
    """
    Category: String Algorithms | Tags: palindrome, filtering | Difficulty: 2

    Return True if `s` is a palindrome when restricted to alphanumeric chars and compared case-insensitively.

    Args:
        s (str): input

    Returns:
        bool: True if palindrome under the rule, else False

    Examples:
        >>> sl_05_is_palindrome_alnum_casefold("Madam, I'm Adam")
        True
        >>> sl_05_is_palindrome_alnum_casefold("Chicago")
        False
    """
    raise ValueError("TODO: implement sl_05_is_palindrome_alnum_casefold")


def sl_06_run_length_encode(s: str) -> str:
    """
    Category: String Algorithms | Tags: encoding, compression | Difficulty: 3

    Produce a simple run-length encoding: consecutive runs as "<char><count>". Use the literal count (no grouping rules).

    Args:
        s (str): input

    Returns:
        str: encoded string

    Examples:
        >>> sl_06_run_length_encode("aaabbc")
        'a3b2c1'
        >>> sl_06_run_length_encode("")
        ''
    """
    raise ValueError("TODO: implement sl_06_run_length_encode")


def sl_07_compress_spaces(s: str) -> str:
    """
    Category: String Cleanup | Tags: whitespace, normalization | Difficulty: 1

    Collapse any run of whitespace to a single space and strip leading/trailing whitespace.

    Args:
        s (str): input

    Returns:
        str: normalized string

    Examples:
        >>> sl_07_compress_spaces("  a   b  c  ")
        'a b c'
        >>> sl_07_compress_spaces("")
        ''
    """
    raise ValueError("TODO: implement sl_07_compress_spaces")


def sl_08_longest_common_prefix(strs: List[str]) -> str:
    """
    Category: String Algorithms | Tags: prefix, lists | Difficulty: 3

    Return the longest common prefix of all strings in `strs`. If `strs` is empty, return ''.

    Args:
        strs (List[str]): list of strings

    Returns:
        str: longest common prefix (possibly empty)

    Examples:
        >>> sl_08_longest_common_prefix(["flower","flow","flight"])
        'fl'
        >>> sl_08_longest_common_prefix(["dog","racecar","car"])
        ''
    """
    raise ValueError("TODO: implement sl_08_longest_common_prefix")


# -----------------------------
# Lists — Basics & Algorithms
# -----------------------------

def sl_09_rotate_right(lst: List[Any], k: int) -> List[Any]:
    """
    Category: List Algorithms | Tags: rotation, indexing | Difficulty: 2

    Rotate `lst` to the right by `k` steps. For k <= 0 or empty list, return a shallow copy of lst.

    Args:
        lst (List[Any]): input list
        k (int): steps to rotate right

    Returns:
        List[Any]: rotated list

    Examples:
        >>> sl_09_rotate_right([1,2,3,4,5], 2)
        [4, 5, 1, 2, 3]
        >>> sl_09_rotate_right([], 5)
        []
    """
    raise ValueError("TODO: implement sl_09_rotate_right")


def sl_10_dedupe_preserve_order(lst: List[Any]) -> List[Any]:
    """
    Category: List Basics | Tags: set-like, stability | Difficulty: 2

    Remove duplicates while preserving first occurrence order.

    Args:
        lst (List[Any]): input list

    Returns:
        List[Any]: list with first occurrences only

    Examples:
        >>> sl_10_dedupe_preserve_order([1,2,1,3,2,4])
        [1, 2, 3, 4]
        >>> sl_10_dedupe_preserve_order([])
        []
    """
    raise ValueError("TODO: implement sl_10_dedupe_preserve_order")


def sl_11_flatten_once(list_of_lists: List[List[Any]]) -> List[Any]:
    """
    Category: List Basics | Tags: flatten, one-level | Difficulty: 1

    Flatten a list of lists by one level (no deep recursion).

    Args:
        list_of_lists (List[List[Any]]): nested lists (one level)

    Returns:
        List[Any]: flattened list

    Examples:
        >>> sl_11_flatten_once([[1,2],[3],[4,5]])
        [1, 2, 3, 4, 5]
        >>> sl_11_flatten_once([])
        []
    """
    raise ValueError("TODO: implement sl_11_flatten_once")


def sl_12_pairwise_sum(a: List[int], b: List[int]) -> List[int]:
    """
    Category: List Algorithms | Tags: elementwise, zip | Difficulty: 1

    Return elementwise sums up to the length of the shorter list.

    Args:
        a (List[int]): first list
        b (List[int]): second list

    Returns:
        List[int]: pairwise sums

    Examples:
        >>> sl_12_pairwise_sum([1,2,3],[10,20])
        [11, 22]
        >>> sl_12_pairwise_sum([], [1,2])
        []
    """
    raise ValueError("TODO: implement sl_12_pairwise_sum")


def sl_13_window_sums(lst: List[int], k: int) -> List[int]:
    """
    Category: List Algorithms | Tags: sliding-window | Difficulty: 3

    Return sums of each contiguous window of size k (k>=1). If len(lst) < k, return [].

    Args:
        lst (List[int]): numbers
        k (int): window size (>=1)

    Returns:
        List[int]: list of window sums

    Examples:
        >>> sl_13_window_sums([1,2,3,4,5], 3)
        [6, 9, 12]
        >>> sl_13_window_sums([1,2], 3)
        []
    """
    raise ValueError("TODO: implement sl_13_window_sums")


def sl_14_mode_smallest_on_tie(lst: List[int]) -> Optional[int]:
    """
    Category: List Algorithms | Tags: frequency, statistics | Difficulty: 2

    Return the mode of `lst`. On ties, return the smallest value. For empty list, return None.

    Args:
        lst (List[int]): values

    Returns:
        Optional[int]: mode or None if empty

    Examples:
        >>> sl_14_mode_smallest_on_tie([1,1,2,2,3])
        1
        >>> sl_14_mode_smallest_on_tie([]) is None
        True
    """
    raise ValueError("TODO: implement sl_14_mode_smallest_on_tie")


def sl_15_unique_sorted(lst: List[int]) -> List[int]:
    """
    Category: List Basics | Tags: sorting, dedupe | Difficulty: 1

    Return a sorted list of unique elements from `lst`.

    Args:
        lst (List[int]): values

    Returns:
        List[int]: sorted unique elements

    Examples:
        >>> sl_15_unique_sorted([3,1,2,1,3])
        [1, 2, 3]
        >>> sl_15_unique_sorted([])
        []
    """
    raise ValueError("TODO: implement sl_15_unique_sorted")


def sl_16_list_median(lst: List[float]) -> Optional[float]:
    """
    Category: List Algorithms | Tags: median, sorting | Difficulty: 2

    Return median of numbers. For even length, return the average of the two middle values as float. Empty -> None.

    Args:
        lst (List[float]): numbers

    Returns:
        Optional[float]: median or None if empty

    Examples:
        >>> sl_16_list_median([3,1,2])
        2
        >>> sl_16_list_median([1,2,3,4])
        2.5
    """
    raise ValueError("TODO: implement sl_16_list_median")


def sl_17_interleave_zip_longest(a: List[Any], b: List[Any], fill: Optional[Any] = None) -> List[Any]:
    """
    Category: List Algorithms | Tags: interleave, zip_longest | Difficulty: 2

    Interleave elements of `a` and `b`. If lengths differ, append remaining elements from the longer list; when one side
    is exhausted, use `fill` for the missing side.

    Args:
        a (List[Any]): first list
        b (List[Any]): second list
        fill (Any | None): value to fill when one list is shorter

    Returns:
        List[Any]: interleaved list

    Examples:
        >>> sl_17_interleave_zip_longest([1,2,3],["a","b"])  # default fill None
        [1, 'a', 2, 'b', 3, None]
        >>> sl_17_interleave_zip_longest([1],[2,3,4], fill=0)
        [1, 2, 0, 3, 0, 4]
    """
    raise ValueError("TODO: implement sl_17_interleave_zip_longest")


def sl_18_two_sum_indices(lst: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Category: List Algorithms | Tags: hashing, two-sum | Difficulty: 3

    Return indices (i, j) with i < j such that lst[i] + lst[j] == target. If none, return None.

    Args:
        lst (List[int]): numbers
        target (int): desired sum

    Returns:
        Optional[Tuple[int,int]]: pair of indices or None

    Examples:
        >>> sl_18_two_sum_indices([2,7,11,15], 9)
        (0, 1)
        >>> sl_18_two_sum_indices([1,2,3], 7) is None
        True
    """
    raise ValueError("TODO: implement sl_18_two_sum_indices")


# -----------------------------
# Hybrid (Strings ⇄ Lists)
# -----------------------------

def sl_19_word_frequencies(text: str) -> List[Tuple[str, int]]:
    """
    Category: Hybrid | Tags: tokenization, counts, normalization | Difficulty: 3

    Tokenize on non-alphanumeric boundaries; normalize to lowercase; return a list of (word, count) sorted by
    decreasing count then alphabetically.

    Args:
        text (str): input text

    Returns:
        List[Tuple[str,int]]: sorted frequency list

    Examples:
        >>> sl_19_word_frequencies("To be, or not to be?")
        [('be', 2), ('to', 2), ('not', 1), ('or', 1)]
        >>> sl_19_word_frequencies("")
        []
    """
    raise ValueError("TODO: implement sl_19_word_frequencies")


def sl_20_top_k_words(text: str, k: int) -> List[str]:
    """
    Category: Hybrid | Tags: tokenization, top-k | Difficulty: 2

    Return the top-k most frequent words (lowercased). Break ties by alphabetical order. If k <= 0, return [].

    Args:
        text (str): input text
        k (int): number of words to return

    Returns:
        List[str]: top-k words by frequency

    Examples:
        >>> sl_20_top_k_words("a a b b b C c")
        ['b', 'a', 'c']
        >>> sl_20_top_k_words("", 5)
        []
    """
    raise ValueError("TODO: implement sl_20_top_k_words")


def sl_21_caesar_shift(s: str, k: int) -> str:
    """
    Category: String Transform | Tags: Caesar, shift, wrap | Difficulty: 2

    Shift only alphabetic characters by k positions (wrap within 'a'..'z' and 'A'..'Z'); leave others unchanged.

    Args:
        s (str): input
        k (int): shift (can be negative)

    Returns:
        str: shifted string

    Examples:
        >>> sl_21_caesar_shift("Abc-Z", 2)
        'Cde-B'
        >>> sl_21_caesar_shift("Hello, World!", 13)
        'Uryyb, Jbeyq!'
    """
    raise ValueError("TODO: implement sl_21_caesar_shift")


def sl_22_is_anagram(a: str, b: str) -> bool:
    """
    Category: String Algorithms | Tags: frequency, anagram | Difficulty: 2

    Return True if a and b are anagrams ignoring case and non-alphanumeric characters.

    Args:
        a (str): first string
        b (str): second string

    Returns:
        bool: True if anagrams per rule

    Examples:
        >>> sl_22_is_anagram("Dormitory", "Dirty room!!")
        True
        >>> sl_22_is_anagram("abc", "abz")
        False
    """
    raise ValueError("TODO: implement sl_22_is_anagram")


def sl_23_longest_run_char(s: str) -> Tuple[Optional[str], int]:
    """
    Category: String Algorithms | Tags: runs, counting | Difficulty: 2

    Return (char, length) for the longest consecutive run in s. If s is empty, return (None, 0).
    On ties, choose the earliest run.

    Args:
        s (str): input

    Returns:
        Tuple[Optional[str], int]: (character or None, run length)

    Examples:
        >>> sl_23_longest_run_char("aaabbccccd")
        ('c', 4)
        >>> sl_23_longest_run_char("")
        (None, 0)
    """
    raise ValueError("TODO: implement sl_23_longest_run_char")


def sl_24_longest_palindromic_substring(s: str) -> str:
    """
    Category: String Algorithms | Tags: palindrome, expand-center | Difficulty: 3 | hard

    Return the longest palindromic substring of s. If multiple have same length, return the first by start index.

    Args:
        s (str): input

    Returns:
        str: longest palindromic substring (possibly empty if s is empty)

    Examples:
        >>> sl_24_longest_palindromic_substring("babad") in ("bab", "aba")
        True
        >>> sl_24_longest_palindromic_substring("cbbd")
        'bb'
    """
    raise ValueError("TODO: implement sl_24_longest_palindromic_substring")


def sl_25_most_frequent_char(s: str) -> Optional[str]:
    """
    Category: String Algorithms | Tags: frequency, tie-break | Difficulty: 2

    Return the most frequent character in s; on ties return the lexicographically smallest. Empty -> None.

    Args:
        s (str): input

    Returns:
        Optional[str]: winning character or None

    Examples:
        >>> sl_25_most_frequent_char("abbbbccddeee")
        'b'
        >>> sl_25_most_frequent_char("")
        None
    """
    raise ValueError("TODO: implement sl_25_most_frequent_char")


def sl_26_remove_adjacent_k_duplicates(s: str, k: int) -> str:
    """
    Category: String Algorithms | Tags: stack, dedupe, k-group | Difficulty: 3 | hard

    Repeatedly remove groups of exactly k adjacent equal characters until no more removals are possible.

    Args:
        s (str): input
        k (int): group size (>=2)

    Returns:
        str: reduced string

    Examples:
        >>> sl_26_remove_adjacent_k_duplicates("deeedbbcccbdaa", 3)
        'aa'
        >>> sl_26_remove_adjacent_k_duplicates("pbbcggttciiippooaais", 2)
        'ps'
    """
    raise ValueError("TODO: implement sl_26_remove_adjacent_k_duplicates")


def sl_27_common_characters(a: str, b: str) -> List[str]:
    """
    Category: String Basics | Tags: set, intersection | Difficulty: 1

    Return sorted list of unique characters appearing in both strings (case-sensitive).

    Args:
        a (str): first
        b (str): second

    Returns:
        List[str]: sorted unique common characters

    Examples:
        >>> sl_27_common_characters("abc", "bcd")
        ['b', 'c']
        >>> sl_27_common_characters("", "xyz")
        []
    """
    raise ValueError("TODO: implement sl_27_common_characters")


def sl_28_group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Category: String ↔ Lists | Tags: grouping, sorted-key | Difficulty: 3 | hard

    Group words that are anagrams (case-insensitive) together. Within each group, preserve original order.

    Args:
        words (List[str]): input words

    Returns:
        List[List[str]]: list of groups (each a list)

    Examples:
        >>> sl_28_group_anagrams(["eat","Tea","tan","ate","Nat","bat"])
        [['eat', 'Tea', 'ate'], ['tan', 'Nat'], ['bat']]
        >>> sl_28_group_anagrams([])
        []
    """
    raise ValueError("TODO: implement sl_28_group_anagrams")


def sl_29_reverse_each_word(s: str) -> str:
    """
    Category: String Transform | Tags: words, reverse | Difficulty: 1

    Reverse the characters of each word but keep word order; words separated by single spaces.

    Args:
        s (str): input

    Returns:
        str: transformed

    Examples:
        >>> sl_29_reverse_each_word("ab cd ef")
        'ba dc fe'
        >>> sl_29_reverse_each_word("hello")
        'olleh'
    """
    raise ValueError("TODO: implement sl_29_reverse_each_word")


def sl_30_kth_non_overlapping(s: str, sub: str, k: int) -> int:
    """
    Category: String Algorithms | Tags: substring, indexing | Difficulty: 2

    Return the starting index of the k-th NON-overlapping occurrence of sub in s (1-based k). If fewer than k,
    return -1. sub must be non-empty.

    Args:
        s (str): haystack
        sub (str): needle
        k (int): which occurrence (>=1)

    Returns:
        int: starting index or -1

    Examples:
        >>> sl_30_kth_non_overlapping("aaaaaa", "aa", 3)
        4
        >>> sl_30_kth_non_overlapping("abc", "x", 1)
        -1
    """
    raise ValueError("TODO: implement sl_30_kth_non_overlapping")


def sl_31_strip_outer_parentheses(s: str) -> str:
    """
    Category: String Algorithms | Tags: stack, parentheses | Difficulty: 3 | hard

    Remove one outermost pair of matching parentheses from the whole string if it encloses a balanced string;
    otherwise return s unchanged. Does not modify inner pairs.

    Args:
        s (str): input

    Returns:
        str: with one outer pair removed if applicable

    Examples:
        >>> sl_31_strip_outer_parentheses("(a+(b*c))")
        'a+(b*c)'
        >>> sl_31_strip_outer_parentheses("a+(b*c)")
        'a+(b*c)'
    """
    raise ValueError("TODO: implement sl_31_strip_outer_parentheses")


def sl_35_partition_by_parity(lst: List[int]) -> List[int]:
    """
    Category: List Algorithms | Tags: partition, stability | Difficulty: 2

    Return a new list with all even numbers first (relative order preserved), then all odd numbers (order preserved).

    Args:
        lst (List[int]): numbers

    Returns:
        List[int]: partitioned list

    Examples:
        >>> sl_35_partition_by_parity([3,2,4,1,5])
        [2, 4, 3, 1, 5]
        >>> sl_35_partition_by_parity([])
        []
    """
    raise ValueError("TODO: implement sl_35_partition_by_parity")


def sl_36_max_subarray_sum(lst: List[int]) -> int:
    """
    Category: List Algorithms | Tags: Kadane, prefix-sum | Difficulty: 3

    Return the maximum possible sum of a contiguous subarray (empty subarray not allowed if lst non-empty).
    Empty input -> 0.

    Args:
        lst (List[int]): numbers

    Returns:
        int: maximum subarray sum (or 0 if empty)

    Examples:
        >>> sl_36_max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> sl_36_max_subarray_sum([])
        0
    """
    raise ValueError("TODO: implement sl_36_max_subarray_sum")


def sl_37_longest_increasing_run(lst: List[int]) -> int:
    """
    Category: List Algorithms | Tags: runs, monotonic | Difficulty: 2

    Return the length of the longest strictly increasing contiguous run.

    Args:
        lst (List[int]): numbers

    Returns:
        int: max run length (0 for empty)

    Examples:
        >>> sl_37_longest_increasing_run([1,2,2,3,4,1])
        3
        >>> sl_37_longest_increasing_run([])
        0
    """
    raise ValueError("TODO: implement sl_37_longest_increasing_run")


def sl_38_chunk(lst: List[Any], k: int) -> List[List[Any]]:
    """
    Category: List Algorithms | Tags: chunking | Difficulty: 1

    Split lst into chunks of size k (k>=1); the last chunk may be shorter.

    Args:
        lst (List[Any]): input
        k (int): chunk size (>=1)

    Returns:
        List[List[Any]]: chunks

    Examples:
        >>> sl_38_chunk([1,2,3,4,5], 2)
        [[1, 2], [3, 4], [5]]
        >>> sl_38_chunk([], 3)
        []
    """
    raise ValueError("TODO: implement sl_38_chunk")


def sl_39_transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    """
    Category: Lists of Lists | Tags: matrix, transpose | Difficulty: 2

    Return the transpose of a rectangular matrix (assume all rows have equal length).

    Args:
        matrix (List[List[Any]]): input matrix

    Returns:
        List[List[Any]]: transposed matrix

    Examples:
        >>> sl_39_transpose([[1,2,3],[4,5,6]])
        [[1, 4], [2, 5], [3, 6]]
        >>> sl_39_transpose([])
        []
    """
    raise ValueError("TODO: implement sl_39_transpose")


def sl_40_diagonal_sums(matrix: List[List[int]]) -> Tuple[int, int]:
    """
    Category: Lists of Lists | Tags: matrix, diagonals | Difficulty: 2

    For a square matrix, return (primary_diagonal_sum, secondary_diagonal_sum).
    If matrix is empty, return (0, 0).

    Args:
        matrix (List[List[int]]): square matrix or empty

    Returns:
        Tuple[int, int]: (primary, secondary)

    Examples:
        >>> sl_40_diagonal_sums([[1,2],[3,4]])
        (5, 5)
        >>> sl_40_diagonal_sums([])
        (0, 0)
    """
    raise ValueError("TODO: implement sl_40_diagonal_sums")


def sl_41_rotate_matrix_90_cw(matrix: List[List[Any]]) -> List[List[Any]]:
    """
    Category: Lists of Lists | Tags: matrix, rotation | Difficulty: 3 | hard

    Return a new matrix rotated 90 degrees clockwise. Assume rectangular matrix; treat missing cells as not applicable.

    Args:
        matrix (List[List[Any]]): input matrix

    Returns:
        List[List[Any]]: rotated matrix

    Examples:
        >>> sl_41_rotate_matrix_90_cw([[1,2,3],[4,5,6]])
        [[4, 1], [5, 2], [6, 3]]
        >>> sl_41_rotate_matrix_90_cw([])
        []
    """
    raise ValueError("TODO: implement sl_41_rotate_matrix_90_cw")


def sl_42_merge_sorted(a: List[int], b: List[int]) -> List[int]:
    """
    Category: List Algorithms | Tags: merge, two-pointer | Difficulty: 2

    Merge two sorted ascending lists into a new sorted list.

    Args:
        a (List[int]): first sorted
        b (List[int]): second sorted

    Returns:
        List[int]: merged sorted list

    Examples:
        >>> sl_42_merge_sorted([1,3,5], [2,4,6])
        [1, 2, 3, 4, 5, 6]
        >>> sl_42_merge_sorted([], [])
        []
    """
    raise ValueError("TODO: implement sl_42_merge_sorted")


def sl_43_insertion_index(lst: List[int], x: int) -> int:
    """
    Category: List Algorithms | Tags: binary-search-ish, position | Difficulty: 2

    Return the index where x should be inserted to keep lst sorted ascending (like bisect_left).
    Assume lst is already sorted.

    Args:
        lst (List[int]): sorted ascending
        x (int): value to position

    Returns:
        int: insertion index in [0, len(lst)]

    Examples:
        >>> sl_43_insertion_index([1,2,4,4,5], 4)
        2
        >>> sl_43_insertion_index([], 7)
        0
    """
    raise ValueError("TODO: implement sl_43_insertion_index")


def sl_44_stable_unique_by_key(rows: List[List[Any]], key_index: int) -> List[List[Any]]:
    """
    Category: Lists of Lists | Tags: dedupe, stable, key | Difficulty: 3 | hard

    Given rows as lists, drop subsequent rows whose key (rows[i][key_index]) was seen before; preserve first occurrences
    and the original order.

    Args:
        rows (List[List[Any]]): input rows
        key_index (int): column index to determine uniqueness

    Returns:
        List[List[Any]]: filtered rows

    Examples:
        >>> sl_44_stable_unique_by_key([[1,'a'],[2,'b'],[1,'x'],[3,'b']], 0)
        [[1, 'a'], [2, 'b'], [3, 'b']]
        >>> sl_44_stable_unique_by_key([], 0)
        []
    """
    raise ValueError("TODO: implement sl_44_stable_unique_by_key")


def sl_45_frequency_table(lst: List[Any]) -> List[Tuple[Any, int]]:
    """
    Category: List Algorithms | Tags: counts, sorting | Difficulty: 2

    Return list of (value, count) sorted by decreasing count then by value ascending.

    Args:
        lst (List[Any]): values

    Returns:
        List[Tuple[Any,int]]: frequency table

    Examples:
        >>> sl_45_frequency_table([3,1,2,1,3,3])
        [(3, 3), (1, 2), (2, 1)]
        >>> sl_45_frequency_table([])
        []
    """
    raise ValueError("TODO: implement sl_45_frequency_table")


def sl_46_majority_element(lst: List[Any]) -> Optional[Any]:
    """
    Category: List Algorithms | Tags: majority, Boyer-Moore (concept) | Difficulty: 3

    Return an element that appears strictly more than n/2 times if one exists; else return None.

    Args:
        lst (List[Any]): values

    Returns:
        Optional[Any]: majority element or None

    Examples:
        >>> sl_46_majority_element([2,2,1,2,3,2,2])
        2
        >>> sl_46_majority_element([1,2,3])
        None
    """
    raise ValueError("TODO: implement sl_46_majority_element")


def sl_47_two_sum_all_pairs(lst: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Category: List Algorithms | Tags: hashing, pairs | Difficulty: 3 | hard

    Return all unique index pairs (i, j) with i < j such that lst[i] + lst[j] == target. Sort pairs by i then j.

    Args:
        lst (List[int]): numbers
        target (int): desired sum

    Returns:
        List[Tuple[int,int]]: list of index pairs

    Examples:
        >>> sl_47_two_sum_all_pairs([1,2,3,4,3], 6)
        [(1, 3), (2, 4)]
        >>> sl_47_two_sum_all_pairs([], 10)
        []
    """
    raise ValueError("TODO: implement sl_47_two_sum_all_pairs")


def sl_48_sliding_window_max(lst: List[int], k: int) -> List[int]:
    """
    Category: List Algorithms | Tags: sliding-window, deque | Difficulty: 3 | hard

    Return the maximum of each window of size k (k>=1). If len(lst) < k, return [].

    Args:
        lst (List[int]): numbers
        k (int): window size

    Returns:
        List[int]: window maxima

    Examples:
        >>> sl_48_sliding_window_max([1,3,-1,-3,5,3,6,7], 3)
        [3, 3, 5, 5, 6, 7]
        >>> sl_48_sliding_window_max([2,1], 3)
        []
    """
    raise ValueError("TODO: implement sl_48_sliding_window_max")


def sl_49_matrix_is_magic_square(matrix: List[List[int]]) -> bool:
    """
    Category: Lists of Lists | Tags: matrix, validation | Difficulty: 3 | hard

    Return True if the given square matrix is a magic square (all rows, columns, and the two diagonals
    sum to the same value and contains the integers 1..n^2 exactly once). Empty -> False.

    Args:
        matrix (List[List[int]]): square matrix

    Returns:
        bool: True if magic square

    Examples:
        >>> sl_49_matrix_is_magic_square([[8,1,6],[3,5,7],[4,9,2]])
        True
        >>> sl_49_matrix_is_magic_square([[1,2],[3,4]])
        False
    """
    raise ValueError("TODO: implement sl_49_matrix_is_magic_square")


def sl_32_word_wrap(text: str, width: int) -> List[str]:
    """
    Category: Hybrid | Tags: wrapping, greedy | Difficulty: 3 | hard

    Wrap text into lines of length at most width (width>=1) without breaking words; words are separated by spaces.
    Distribute words greedily; no hyphenation. Collapse multiple spaces in input to single spaces for wrapping.

    Args:
        text (str): input text
        width (int): max line width

    Returns:
        List[str]: wrapped lines

    Examples:
        >>> sl_32_word_wrap("a bb ccc dddd", 5)
        ['a bb', 'ccc', 'dddd']
        >>> sl_32_word_wrap("", 10)
        []
    """
    raise ValueError("TODO: implement sl_32_word_wrap")


def sl_33_ngram_counts(text: str, n: int) -> List[Tuple[str, int]]:
    """
    Category: Hybrid | Tags: n-grams, frequency | Difficulty: 3

    Return frequency list of lowercase character n-grams (continuous substrings of length n) from alphanumeric-only
    text (remove non-alphanumerics first). Sort by decreasing count then lexicographically.

    Args:
        text (str): input
        n (int): n-gram length (>=1)

    Returns:
        List[Tuple[str,int]]: (ngram, count) sorted

    Examples:
        >>> sl_33_ngram_counts("ABAB!", 2)
        [('ab', 2), ('ba', 1)]
        >>> sl_33_ngram_counts("", 3)
        []
    """
    raise ValueError("TODO: implement sl_33_ngram_counts")


def sl_34_top_k_bigrams(text: str, k: int) -> List[Tuple[Tuple[str,str], int]]:
    """
    Category: Hybrid | Tags: bigrams, frequency, top-k | Difficulty: 3

    Tokenize text on non-alphanumeric boundaries (lowercased). Compute bigram counts of consecutive words and
    return the top-k as [((w1, w2), count), ...] sorted by decreasing count then alphabetically by (w1,w2).
    If k <= 0 or fewer than k bigrams exist, return all.

    Args:
        text (str): input
        k (int): number of bigrams to return

    Returns:
        List[Tuple[Tuple[str,str], int]]: top-k bigrams with counts

    Examples:
        >>> sl_34_top_k_bigrams("to be or not to be", 2)
        [(('to', 'be'), 2), (('be', 'or'), 1)]
        >>> sl_34_top_k_bigrams("", 5)
        []
    """
    raise ValueError("TODO: implement sl_34_top_k_bigrams")


def sl_50_longest_common_suffix(strs: List[str]) -> str:
    """
    Category: Hybrid | Tags: suffix, strings | Difficulty: 2

    Return the longest common suffix among all strings. Empty list -> ''.

    Args:
        strs (List[str]): list of strings

    Returns:
        str: longest common suffix

    Examples:
        >>> sl_50_longest_common_suffix(["running","jogging","ping"])
        'ing'
        >>> sl_50_longest_common_suffix(["abc","def"])
        ''
    """
    raise ValueError("TODO: implement sl_50_longest_common_suffix")


def sl_51_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Category: String Algorithms | Tags: sliding-window, hashmap | Difficulty: 4 | very hard

    Return the length of the longest substring that contains at most k distinct characters.
    If k <= 0, return 0.

    Args:
        s (str): input string
        k (int): maximum number of distinct characters allowed

    Returns:
        int: length of the longest valid substring

    Examples:
        >>> sl_51_longest_substring_k_distinct("eceba", 2)
        3
        >>> sl_51_longest_substring_k_distinct("aa", 1)
        2
    """
    raise ValueError("TODO: implement sl_51_longest_substring_k_distinct")


def sl_52_min_window_substring(s: str, t: str) -> str:
    """
    Category: String Algorithms | Tags: sliding-window, frequency | Difficulty: 4 | very hard

    Return the minimum window in `s` that contains all the characters of `t` (with multiplicity).
    If no such window exists, return an empty string. Case-sensitive.

    Args:
        s (str): haystack
        t (str): pattern to cover (may contain duplicates)

    Returns:
        str: smallest window substring or '' if impossible

    Examples:
        >>> sl_52_min_window_substring("ADOBECODEBANC", "ABC")
        'BANC'
        >>> sl_52_min_window_substring("a", "aa")
        ''
    """
    raise ValueError("TODO: implement sl_52_min_window_substring")


def sl_53_remove_min_to_make_valid_parentheses(s: str) -> str:
    """
    Category: String Cleanup | Tags: stack, parentheses | Difficulty: 4 | very hard

    Remove the minimum number of parentheses so that the result is a valid parentheses string.
    Letters and other characters should remain in place.

    Args:
        s (str): input string possibly containing '(', ')', and letters

    Returns:
        str: a valid parentheses string with minimal removals

    Examples:
        >>> sl_53_remove_min_to_make_valid_parentheses("a)b(c)d")
        'ab(c)d'
        >>> sl_53_remove_min_to_make_valid_parentheses(")a((b)c(")
        'a(b)c'
    """
    raise ValueError("TODO: implement sl_53_remove_min_to_make_valid_parentheses")


def sl_54_smallest_subsequence_distinct(s: str) -> str:
    """
    Category: String Algorithms | Tags: monotonic-stack, greedy | Difficulty: 4 | very hard

    Return the lexicographically smallest subsequence of `s` that contains all the distinct characters of `s`
    exactly once.

    Args:
        s (str): input string

    Returns:
        str: smallest subsequence containing each distinct char once

    Examples:
        >>> sl_54_smallest_subsequence_distinct("cbacdcbc")
        'acdb'
        >>> sl_54_smallest_subsequence_distinct("bcabc")
        'abc'
    """
    raise ValueError("TODO: implement sl_54_smallest_subsequence_distinct")


def sl_55_decode_string_nested(s: str) -> str:
    """
    Category: String Algorithms | Tags: stack, parsing | Difficulty: 4 | very hard

    Decode an encoded string with nested repetition counts, where patterns are of the form k[encoded_string].
    Assume k is a positive integer and nesting is valid. Non-bracket chars copy through.

    Args:
        s (str): encoded input, e.g., '3[a2[c]]'

    Returns:
        str: decoded string

    Examples:
        >>> sl_55_decode_string_nested("3[a]2[bc]")
        'aaabcbc'
        >>> sl_55_decode_string_nested("3[a2[c]]")
        'accaccacc'
    """
    raise ValueError("TODO: implement sl_55_decode_string_nested")


def sl_56_longest_repeating_char_replacement(s: str, k: int) -> int:
    """
    Category: String Algorithms | Tags: sliding-window, frequency | Difficulty: 4 | very hard

    Given a string consisting of uppercase letters, return the length of the longest substring you can obtain by
    replacing at most k characters so that all characters in the substring are the same.

    Args:
        s (str): uppercase letters string
        k (int): maximum number of replacements

    Returns:
        int: maximum length achievable

    Examples:
        >>> sl_56_longest_repeating_char_replacement("ABAB", 2)
        4
        >>> sl_56_longest_repeating_char_replacement("AABABBA", 1)
        4
    """
    raise ValueError("TODO: implement sl_56_longest_repeating_char_replacement")


def sl_57_trap_rain_water(heights: List[int]) -> int:
    """
    Category: List Algorithms | Tags: two-pointers, prefix-suffix | Difficulty: 4 | very hard

    Given non-negative integers representing an elevation map, compute how much water it can trap after raining.

    Args:
        heights (List[int]): elevation heights

    Returns:
        int: total trapped water units

    Examples:
        >>> sl_57_trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1])
        6
        >>> sl_57_trap_rain_water([])
        0
    """
    raise ValueError("TODO: implement sl_57_trap_rain_water")


def sl_58_subarray_sum_equals_k_count(nums: List[int], k: int) -> int:
    """
    Category: List Algorithms | Tags: prefix-sum, hashmap | Difficulty: 4 | very hard

    Return the total number of contiguous subarrays whose sum equals k.

    Args:
        nums (List[int]): list of integers (may include negatives)
        k (int): target sum

    Returns:
        int: count of qualifying subarrays

    Examples:
        >>> sl_58_subarray_sum_equals_k_count([1,1,1], 2)
        2
        >>> sl_58_subarray_sum_equals_k_count([1,2,3], 3)
        2
    """
    raise ValueError("TODO: implement sl_58_subarray_sum_equals_k_count")


def sl_59_lis_length_nlogn(lst: List[int]) -> int:
    """
    Category: List Algorithms | Tags: LIS, patience-sorting | Difficulty: 4 | very hard

    Return the length of the Longest Increasing Subsequence of lst using an O(n log n) approach.

    Args:
        lst (List[int]): numbers

    Returns:
        int: length of LIS (0 for empty)

    Examples:
        >>> sl_59_lis_length_nlogn([10,9,2,5,3,7,101,18])
        4
        >>> sl_59_lis_length_nlogn([])
        0
    """
    raise ValueError("TODO: implement sl_59_lis_length_nlogn")


def sl_60_matrix_spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Category: Lists of Lists | Tags: matrix, traversal | Difficulty: 4 | very hard

    Return all elements of the matrix in spiral order (clockwise, starting from top-left). For empty matrix, return [].

    Args:
        matrix (List[List[int]]): 2D list

    Returns:
        List[int]: spiral order traversal

    Examples:
        >>> sl_60_matrix_spiral_order([[1,2,3],[4,5,6],[7,8,9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        >>> sl_60_matrix_spiral_order([])
        []
    """
    raise ValueError("TODO: implement sl_60_matrix_spiral_order")
