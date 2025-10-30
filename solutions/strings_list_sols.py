

from typing import List, Tuple, Optional, Any, Dict, Set
from collections import Counter, deque, OrderedDict
import re
import math

# -----------------------------
# Strings — Basics & Algorithms
# -----------------------------

def sl_01_count_vowels(s: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)


def sl_02_count_substring_overlapping(s: str, sub: str) -> int:
    if not sub:
        raise ValueError("sub must be non-empty")
    count = 0
    i = 0
    n, m = len(s), len(sub)
    while i + m <= n:
        if s[i:i+m] == sub:
            count += 1
        i += 1
    return count


def sl_03_first_unique_char_index(s: str) -> int:
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


def sl_04_reverse_words(s: str) -> str:
    parts = s.split()
    parts.reverse()
    return " ".join(parts)


def sl_05_is_palindrome_alnum_casefold(s: str) -> bool:
    filtered = [c.casefold() for c in s if c.isalnum()]
    return filtered == filtered[::-1]


def sl_06_run_length_encode(s: str) -> str:
    if not s:
        return ""
    out = []
    prev = s[0]
    cnt = 1
    for c in s[1:]:
        if c == prev:
            cnt += 1
        else:
            out.append(f"{prev}{cnt}")
            prev = c
            cnt = 1
    out.append(f"{prev}{cnt}")
    return "".join(out)


def sl_07_compress_spaces(s: str) -> str:
    return " ".join(s.split())


def sl_08_longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest

# -----------------------------
# Lists — Basics & Algorithms
# -----------------------------

def sl_09_rotate_right(lst: List[Any], k: int) -> List[Any]:
    n = len(lst)
    if n == 0 or k <= 0:
        return lst[:]
    k %= n
    if k == 0:
        return lst[:]
    return lst[-k:] + lst[:-k]


def sl_10_dedupe_preserve_order(lst: List[Any]) -> List[Any]:
    seen: Set[Any] = set()
    out: List[Any] = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def sl_11_flatten_once(list_of_lists: List[List[Any]]) -> List[Any]:
    out: List[Any] = []
    for sub in list_of_lists:
        out.extend(sub)
    return out


def sl_12_pairwise_sum(a: List[int], b: List[int]) -> List[int]:
    return [x + y for x, y in zip(a, b)]


def sl_13_window_sums(lst: List[int], k: int) -> List[int]:
    if k <= 0 or len(lst) < k:
        return []
    window = sum(lst[:k])
    out = [window]
    for i in range(k, len(lst)):
        window += lst[i] - lst[i - k]
        out.append(window)
    return out


def sl_14_mode_smallest_on_tie(lst: List[int]) -> Optional[int]:
    if not lst:
        return None
    freq = Counter(lst)
    max_count = max(freq.values())
    candidates = [x for x, c in freq.items() if c == max_count]
    return min(candidates)


def sl_15_unique_sorted(lst: List[int]) -> List[int]:
    return sorted(set(lst))


def sl_16_list_median(lst: List[float]) -> Optional[float]:
    if not lst:
        return None
    a = sorted(lst)
    n = len(a)
    mid = n // 2
    if n % 2 == 1:
        return float(a[mid]) if isinstance(a[mid], bool) else a[mid]
    return (a[mid - 1] + a[mid]) / 2


def sl_17_interleave_zip_longest(a: List[Any], b: List[Any], fill: Optional[Any] = None) -> List[Any]:
    n = max(len(a), len(b))
    out: List[Any] = []
    for i in range(n):
        out.append(a[i] if i < len(a) else fill)
        out.append(b[i] if i < len(b) else fill)
    return out


def sl_18_two_sum_indices(lst: List[int], target: int) -> Optional[Tuple[int, int]]:
    seen: Dict[int, int] = {}
    for j, v in enumerate(lst):
        need = target - v
        if need in seen:
            return (seen[need], j)
        if v not in seen:
            seen[v] = j
    return None

# -----------------------------
# Hybrid (Strings ⇄ Lists)
# -----------------------------

_word_re = re.compile(r"[A-Za-z0-9]+")

def _tokenize(text: str) -> List[str]:
    return [m.group(0).lower() for m in _word_re.finditer(text or "")]


def sl_19_word_frequencies(text: str) -> List[Tuple[str, int]]:
    words = _tokenize(text)
    if not words:
        return []
    cnt = Counter(words)
    return sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))


def sl_20_top_k_words(text: str, k: int) -> List[str]:
    if k <= 0:
        return []
    return [w for w, _ in sl_19_word_frequencies(text)[:k]]


def sl_21_caesar_shift(s: str, k: int) -> str:
    def shift_char(ch: str) -> str:
        if 'a' <= ch <= 'z':
            base = ord('a')
            return chr(base + (ord(ch) - base + k) % 26)
        if 'A' <= ch <= 'Z':
            base = ord('A')
            return chr(base + (ord(ch) - base + k) % 26)
        return ch
    return "".join(shift_char(c) for c in s)


def sl_22_is_anagram(a: str, b: str) -> bool:
    fa = Counter(c.lower() for c in a if c.isalnum())
    fb = Counter(c.lower() for c in b if c.isalnum())
    return fa == fb


def sl_23_longest_run_char(s: str) -> Tuple[Optional[str], int]:
    if not s:
        return (None, 0)
    best_char = s[0]
    best_len = 1
    cur_char = s[0]
    cur_len = 1
    for c in s[1:]:
        if c == cur_char:
            cur_len += 1
        else:
            if cur_len > best_len:
                best_char, best_len = cur_char, cur_len
            cur_char, cur_len = c, 1
    if cur_len > best_len:
        best_char, best_len = cur_char, cur_len
    return (best_char, best_len)


def sl_24_longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""
    def expand(l: int, r: int) -> Tuple[int, int]:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r  # [start, end)
    best = (0, 1)
    for i in range(len(s)):
        a = expand(i, i)
        b = expand(i, i + 1)
        cand = max(a, b, key=lambda t: t[1] - t[0])
        if cand[1] - cand[0] > best[1] - best[0]:
            best = cand
    return s[best[0]:best[1]]


def sl_25_most_frequent_char(s: str) -> Optional[str]:
    if not s:
        return None
    cnt = Counter(s)
    max_count = max(cnt.values())
    candidates = [ch for ch, c in cnt.items() if c == max_count]
    return min(candidates)


def sl_26_remove_adjacent_k_duplicates(s: str, k: int) -> str:
    if k <= 1:
        return ""
    stack: List[Tuple[str, int]] = []
    for ch in s:
        if stack and stack[0] and stack[-1][0] == ch:
            c = stack[-1][1] + 1
            stack[-1] = (ch, c)
            if c == k:
                stack.pop()
        else:
            stack.append((ch, 1))
    return "".join(ch * c for ch, c in stack)


def sl_27_common_characters(a: str, b: str) -> List[str]:
    return sorted(set(a) & set(b))


def sl_28_group_anagrams(words: List[str]) -> List[List[str]]:
    groups: "OrderedDict[str, List[str]]" = OrderedDict()
    first_seen_order: List[str] = []
    for w in words:
        key = "".join(sorted(w.lower()))
        if key not in groups:
            groups[key] = []
            first_seen_order.append(key)
        groups[key].append(w)
    return [groups[key] for key in first_seen_order]


def sl_29_reverse_each_word(s: str) -> str:
    if not s:
        return s
    # Words separated by single spaces per spec
    return " ".join(word[::-1] for word in s.split(" "))


def sl_30_kth_non_overlapping(s: str, sub: str, k: int) -> int:
    if not sub or k < 1:
        return -1
    start = 0
    for _ in range(k):
        idx = s.find(sub, start)
        if idx == -1:
            return -1
        start = idx + len(sub)
    return idx


def sl_31_strip_outer_parentheses(s: str) -> str:
    # consider only parentheses to check if the entire string is wrapped by a single outer pair
    if len(s) < 2 or s[0] != '(' or s[-1] != ')':
        return s
    # Check that the outermost pair only closes at the end
    bal = 0
    for i, ch in enumerate(s):
        if ch == '(':
            bal += 1
        elif ch == ')':
            bal -= 1
        if bal == 0 and i != len(s) - 1:
            return s  # closed early
    if bal != 0:
        return s
    return s[1:-1]

# -----------------------------
# More List Algorithms
# -----------------------------

def sl_35_partition_by_parity(lst: List[int]) -> List[int]:
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return evens + odds


def sl_36_max_subarray_sum(lst: List[int]) -> int:
    if not lst:
        return 0
    best = cur = lst[0]
    for x in lst[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def sl_37_longest_increasing_run(lst: List[int]) -> int:
    if not lst:
        return 0
    best = cur = 1
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            cur += 1
        else:
            best = max(best, cur)
            cur = 1
    best = max(best, cur)
    return best


def sl_38_chunk(lst: List[Any], k: int) -> List[List[Any]]:
    if k <= 0:
        raise ValueError("k must be >= 1")
    return [lst[i:i+k] for i in range(0, len(lst), k)]


def sl_39_transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    if not matrix:
        return []
    return [list(col) for col in zip(*matrix)]


def sl_40_diagonal_sums(matrix: List[List[int]]) -> Tuple[int, int]:
    if not matrix:
        return (0, 0)
    n = len(matrix)
    primary = sum(matrix[i][i] for i in range(n))
    secondary = sum(matrix[i][n - 1 - i] for i in range(n))
    return (primary, secondary)


def sl_41_rotate_matrix_90_cw(matrix: List[List[Any]]) -> List[List[Any]]:
    if not matrix:
        return []
    # For rectangular, rotate CW by reversing each column of the transpose
    transposed = [list(col) for col in zip(*matrix)]
    return [list(reversed(row)) for row in transposed]


def sl_42_merge_sorted(a: List[int], b: List[int]) -> List[int]:
    i = j = 0
    out: List[int] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out


def sl_43_insertion_index(lst: List[int], x: int) -> int:
    lo, hi = 0, len(lst)
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def sl_44_stable_unique_by_key(rows: List[List[Any]], key_index: int) -> List[List[Any]]:
    seen: Set[Any] = set()
    out: List[List[Any]] = []
    for r in rows:
        key = r[key_index]
        if key not in seen:
            seen.add(key)
            out.append(r)
    return out


def sl_45_frequency_table(lst: List[Any]) -> List[Tuple[Any, int]]:
    if not lst:
        return []
    cnt = Counter(lst)
    return sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))


def sl_46_majority_element(lst: List[Any]) -> Optional[Any]:
    if not lst:
        return None
    # Boyer-Moore majority vote
    candidate = None
    count = 0
    for x in lst:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    if candidate is not None and lst.count(candidate) > len(lst) // 2:
        return candidate
    return None


def sl_47_two_sum_all_pairs(lst: List[int], target: int) -> List[Tuple[int, int]]:
    pairs: List[Tuple[int, int]] = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] + lst[j] == target:
                pairs.append((i, j))
    pairs.sort()
    return pairs


def sl_48_sliding_window_max(lst: List[int], k: int) -> List[int]:
    n = len(lst)
    if k <= 0 or n < k:
        return []
    dq: deque[int] = deque()  # store indices, values decreasing
    out: List[int] = []
    for i, val in enumerate(lst):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and lst[dq[-1]] <= val:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(lst[dq[0]])
    return out


def sl_49_matrix_is_magic_square(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    if n == 0:
        return False
    if any(len(row) != n for row in matrix):
        return False
    flat = [x for row in matrix for x in row]
    if sorted(flat) != list(range(1, n * n + 1)):
        return False
    target = sum(matrix[0])
    # rows
    if any(sum(row) != target for row in matrix):
        return False
    # columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != target:
            return False
    # diagonals
    if sum(matrix[i][i] for i in range(n)) != target:
        return False
    if sum(matrix[i][n - 1 - i] for i in range(n)) != target:
        return False
    return True


def sl_32_word_wrap(text: str, width: int) -> List[str]:
    if width <= 0 or not text:
        return []
    words = " ".join(text.split()).split(" ")
    lines: List[str] = []
    cur = ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= width:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def sl_33_ngram_counts(text: str, n: int) -> List[Tuple[str, int]]:
    if n <= 0:
        return []
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    if len(cleaned) < n:
        return []
    cnt: Dict[str, int] = {}
    for i in range(len(cleaned) - n + 1):
        gram = cleaned[i:i+n]
        cnt[gram] = cnt.get(gram, 0) + 1
    return sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))


def sl_34_top_k_bigrams(text: str, k: int) -> List[Tuple[Tuple[str, str], int]]:
    if k == 0:
        return []
    words = _tokenize(text)
    big: Dict[Tuple[str, str], int] = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i+1])
        big[pair] = big.get(pair, 0) + 1
    items = sorted(big.items(), key=lambda kv: (-kv[1], kv[0][0], kv[0][1]))
    if k < 0 or k >= len(items):
        return items
    return items[:k]


def sl_50_longest_common_suffix(strs: List[str]) -> str:
    if not strs:
        return ""
    rev = [s[::-1] for s in strs]
    pref = sl_08_longest_common_prefix(rev)
    return pref[::-1]


def sl_51_longest_substring_k_distinct(s: str, k: int) -> int:
    if k <= 0:
        return 0
    left = 0
    counts: Dict[str, int] = {}
    best = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        while len(counts) > k:
            lc = s[left]
            counts[lc] -= 1
            if counts[lc] == 0:
                del counts[lc]
            left += 1
        best = max(best, right - left + 1)
    return best


def sl_52_min_window_substring(s: str, t: str) -> str:
    if not s or not t:
        return ""
    need = Counter(t)
    have: Dict[str, int] = {}
    required = len(need)
    formed = 0
    left = 0
    best_len = math.inf
    best = (0, 0)
    for right, ch in enumerate(s):
        have[ch] = have.get(ch, 0) + 1
        if ch in need and have[ch] == need[ch]:
            formed += 1
        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best = (left, right + 1)
            lc = s[left]
            have[lc] -= 1
            if lc in need and have[lc] < need[lc]:
                formed -= 1
            left += 1
    return s[best[0]:best[1]] if best_len != math.inf else ""


def sl_53_remove_min_to_make_valid_parentheses(s: str) -> str:
    to_remove: Set[int] = set()
    stack: List[int] = []
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    to_remove.update(stack)
    return "".join(ch for i, ch in enumerate(s) if i not in to_remove)


def sl_54_smallest_subsequence_distinct(s: str) -> str:
    last: Dict[str, int] = {ch: i for i, ch in enumerate(s)}
    in_stack: Set[str] = set()
    st: List[str] = []
    for i, ch in enumerate(s):
        if ch in in_stack:
            continue
        while st and ch < st[-1] and last[st[-1]] > i:
            in_stack.remove(st.pop())
        st.append(ch)
        in_stack.add(ch)
    return "".join(st)


def sl_55_decode_string_nested(s: str) -> str:
    num_stack: List[int] = []
    str_stack: List[str] = []
    cur = ""
    k = 0
    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)
        elif ch == '[':
            num_stack.append(k)
            str_stack.append(cur)
            cur = ""
            k = 0
        elif ch == ']':
            times = num_stack.pop() if num_stack else 1
            prev = str_stack.pop() if str_stack else ""
            cur = prev + cur * times
        else:
            cur += ch
    return cur


def sl_56_longest_repeating_char_replacement(s: str, k: int) -> int:
    counts: Dict[str, int] = {}
    left = 0
    maxf = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        maxf = max(maxf, counts[ch])
        while (right - left + 1) - maxf > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


def sl_57_trap_rain_water(heights: List[int]) -> int:
    n = len(heights)
    if n == 0:
        return 0
    left, right = 0, n - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water += right_max - heights[right]
            right -= 1
    return water


def sl_58_subarray_sum_equals_k_count(nums: List[int], k: int) -> int:
    pref = 0
    count = 0
    seen = Counter({0: 1})
    for x in nums:
        pref += x
        count += seen[pref - k]
        seen[pref] += 1
    return count


def sl_59_lis_length_nlogn(lst: List[int]) -> int:
    if not lst:
        return 0
    tails: List[int] = []
    def bisect_left(a: List[int], x: int) -> int:
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
    for x in lst:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def sl_60_matrix_spiral_order(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    top, left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1
    out: List[int] = []
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            out.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            out.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                out.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                out.append(matrix[i][left])
            left += 1
    return out