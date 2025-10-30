"""
CMSC 14100 — Midterm-Style Practice: Conditionals, Loops, & Core Python (75)
----------------------------------------------------------------------------
Structure: Problems ramp from easy → moderate → slightly harder, matching the
midterm scope (through HW5): types/variables/expressions, functions, conditionals,
loops, strings, lists/tuples, lists-of-lists, function scoping ideas (copy vs mutate).

Student instructions
- Replace each `raise ValueError("todo: <name>")` with a correct implementation.
- Unless stated, do NOT import libraries. Use only techniques seen through HW5.
- Prefer clear, idiomatic Python with short-circuiting and good loop choices.
- Time/space complexity does not need to be optimal unless stated.

TA instructions
- These are designed to be autograded with pytest. Each has precise IO behavior.
- Many problems intentionally mirror common exam patterns: safe division, bounds
  checks, scans, counting, early exit, constructing results, light data wrangling.

Notation
- "iff" means "if and only if". Integers fit typical Python int ranges.
- When docstrings mention examples, these are illustrative not exhaustive.
"""

# ----------------------------- Tier 1: Warm‑ups (1–15) -----------------------------
# Focus: expressions, simple conditionals, tiny loops; easy-to-medium difficulty.

def cl01_sign_word(n: int) -> str:
    """Midterm-style
    Problem: Return a word describing the sign of n.
    Inputs: n (int)
    Output: 'positive' if n>0, 'negative' if n<0, 'zero' otherwise.
    Constraints: Use a simple if/elif/else. No printing.
    Example: cl01_sign_word(5) -> 'positive'; cl01_sign_word(0) -> 'zero'.
    """
    if n > 0:
        return 'positive'
    elif n < 0:
        return 'negative'
    else:
        return 'zero'


def cl02_is_even(n: int) -> bool:
    """Midterm-style
    Problem: Decide if n is even.
    Inputs: n (int)
    Output: True iff n % 2 == 0.
    Note: Use an expression (no if needed). Works for negative integers as well.
    """
    return n % 2 == 0


def cl03_abs_no_abs(n: int) -> int:
    """Midterm-style
    Problem: Compute |n| without using abs().
    Inputs: n (int)
    Output: Nonnegative int equal to the magnitude of n.
    Hint: Conditionals are acceptable here.
    """
    if n < 0:
        return -n
    else:
        return n


def cl04_max2(a: int, b: int) -> int:
    """Midterm-style
    Problem: Return the larger of a and b using a basic conditional.
    Inputs: a, b (int)
    Output: max(a, b).
    """
    if a > b:
        return a
    else:
        return b


def cl05_min3(a: int, b: int, c: int) -> int:
    """Midterm-style
    Problem: Return the minimum of three integers using nested conditionals.
    Inputs: a, b, c (int)
    Output: min among the three.
    """
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


def cl06_in_closed_interval(x: int, lo: int, hi: int) -> bool:
    """Midterm-style
    Problem: Decide membership in [lo, hi].
    Inputs: x, lo, hi (int)
    Output: True iff lo <= x <= hi.
    """
    return lo <= x <= hi


def cl07_safe_div(a: float, b: float) -> float | None:
    """Midterm-style
    Problem: Return a/b unless b==0, in which case return None.
    Inputs: a, b (float)
    Output: quotient or None.
    Edge cases: a can be 0; works with negatives.
    """
    if b == 0:
        return None
    else:
        return a / b


def cl08_parity_word(n: int) -> str:
    """Midterm-style
    Problem: Return 'even' or 'odd' for n.
    Inputs: n (int)
    Output: 'even' if divisible by 2 else 'odd'.
    """
    return 'even' if n % 2 == 0 else 'odd'


def cl09_same_parity(a: int, b: int) -> bool:
    """Midterm-style
    Problem: True iff a and b have the same parity.
    Inputs: a, b (int)
    Output: True when both even or both odd.
    """
    return (a % 2) == (b % 2)


def cl10_last_digit(n: int) -> int:
    """Midterm-style
    Problem: Return the last decimal digit of a (possibly negative) integer n.
    Inputs: n (int)
    Output: int in [0,9]. For n=-123, answer is 3.
    Implementation hint: Use % 10 carefully.
    """
    return abs(n) % 10


def cl11_c_to_f(c: float) -> float:
    """Midterm-style
    Problem: Convert Celsius to Fahrenheit using 9/5*c + 32 (float math).
    Inputs: c (float)
    Output: float temperature in Fahrenheit.
    """
    return (9.0/5.0)*c + 32.0


def cl12_triangle_area(base: float, height: float) -> float:
    """Midterm-style
    Problem: Return the area of a triangle: 0.5 * base * height.
    Inputs: base, height (float)
    Output: float area. Assume nonnegative inputs.
    """
    return 0.5 * base * height


def cl13_letter_grade(score: float) -> str:
    """Midterm-style
    Problem: Map a numeric score to a letter grade (A/B/C/D/F).
    Inputs: score (float) in [0,100].
    Output: 'A' (>=90), 'B' (80–89.999), 'C' (70–79.999), 'D' (60–69.999), else 'F'.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def cl14_clamp(x: int, lo: int, hi: int) -> int:
    """Midterm-style
    Problem: Clamp x into the closed interval [lo,hi].
    Inputs: x, lo, hi (int), assume lo<=hi.
    Output: lo if x<lo, hi if x>hi, else x.
    """
    if x < lo:
        return lo
    elif x > hi:
        return hi
    else:
        return x


def cl15_exactly_one_true(p: bool, q: bool) -> bool:
    """Midterm-style
    Problem: Logical XOR for two booleans.
    Inputs: p, q (bool)
    Output: True iff exactly one of p, q is True.
    """
    return (p and not q) or (not p and q)


# ------------------------ Tier 2: Conditionals patterns (16–30) ------------------------
# Focus: multi-branch decisions, short-circuiting, sentinel checks; easy→moderate.

def cl16_tax_bracket_rate(income: int) -> int:
    """Midterm-style
    Problem: Return simple tax *rate* (integer percent) based on bracket:
      - income <= 999 → 30
      - 1000..1999   → 40
      - > 1999       → 45
    Inputs: income (int, >=0)
    Output: 30, 40, or 45.
    """
    if income <= 999:
        return 30
    elif income <= 1999:
        return 40
    else:
        return 45


def cl17_three_way_compare(a: int, b: int) -> int:
    """Midterm-style
    Problem: Return -1 if a<b, 0 if a==b, +1 if a>b.
    Inputs: a, b (int)
    Output: -1/0/+1.
    """
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1


def cl18_non_decreasing(a: int, b: int, c: int) -> bool:
    """Midterm-style
    Problem: True iff a <= b <= c.
    Inputs: a, b, c (int)
    Output: bool
    """
    return a <= b <= c


def cl19_between_strict(x: int, a: int, b: int) -> bool:
    """Midterm-style
    Problem: True iff min(a,b) < x < max(a,b).
    Inputs: x, a, b (int)
    Output: bool using comparisons (no loops needed).
    """
    lo = a if a < b else b
    hi = b if a < b else a
    return lo < x < hi


def cl20_ticket_price(age: int, is_student: bool) -> int:
    """Midterm-style
    Problem: Compute a simple ticket price rule.
    Rule: age<6 → 0; age<=18 or is_student → 10; age>=65 → 8; else 15.
    Inputs: age (int>=0), is_student (bool)
    Output: price (int dollars).
    Note: Evaluate in an order that yields intended discounts.
    """
    if age < 6:
        return 0
    elif age <= 18 or is_student:
        return 10
    elif age >= 65:
        return 8
    else:
        return 15


def cl21_close_enough(x: float, y: float, eps: float) -> bool:
    """Midterm-style
    Problem: True iff |x-y| <= eps. You may use abs().
    Inputs: x, y, eps (float) with eps>=0.
    Output: bool.
    """
    return abs(x - y) <= eps


def cl22_plurals(n: int, word: str) -> str:
    """Midterm-style
    Problem: Return a simple English pluralized phrase "<n> <word or word+'s'>".
    Inputs: n (int), word (str). For n==1 use singular, else add 's'.
    Output: e.g., (1, 'cat')->'1 cat', (3, 'cat')->'3 cats'.
    Note: No need for irregular forms; just 's' suffix.
    """
    if n == 1:
        return f"{n} {word}"
    else:
        return f"{n} {word}s"


def cl23_grade_pass_fail(score: float) -> bool:
    """Midterm-style
    Problem: Return True for pass, False for fail under a cutoff.
    Inputs: score (float in [0,100])
    Policy: pass if score >= 60.0 else fail.
    """
    return score >= 60.0


def cl24_safe_index(lst: list, i: int):
    """Midterm-style
    Problem: Safe indexing: return lst[i] if i is a valid index, else None.
    Inputs: lst (list of any), i (int)
    Output: element or None if i<0 or i>=len(lst).
    """
    if 0 <= i < len(lst):
        return lst[i]
    else:
        return None


def cl25_head_or_default(lst: list, default):
    """Midterm-style
    Problem: Return the first element of lst if present; otherwise return default.
    Inputs: lst (list), default (any)
    Output: element or default.
    """
    if len(lst) > 0:
        return lst[0]
    else:
        return default


def cl26_choose_middle(a: int, b: int, c: int) -> int:
    """Midterm-style
    Problem: Return the median (middle) of three distinct ints using comparisons.
    Inputs: a, b, c distinct ints.
    Output: the median value. Use comparisons only (no sorting).
    """
    if (a > b and a < c) or (a < b and a > c):
        return a
    elif (b > a and b < c) or (b < a and b > c):
        return b
    else:
        return c


def cl27_quadrant(x: int, y: int) -> str:
    """Midterm-style
    Problem: Locate a point in the plane.
    Inputs: x, y (int)
    Output: 'I', 'II', 'III', 'IV' for standard quadrants; 'axis' if on any axis; 'origin' if (0,0).
    """
    if x == 0 and y == 0:
        return 'origin'
    elif x == 0 or y == 0:
        return 'axis'
    elif x > 0 and y > 0:
        return 'I'
    elif x < 0 and y > 0:
        return 'II'
    elif x < 0 and y < 0:
        return 'III'
    else:
        return 'IV'


def cl28_fee_cents_round_down(subtotal_cents: int, pct: int) -> int:
    """Midterm-style
    Problem: Compute an integer fee by percent, floor-rounded.
    Inputs: subtotal_cents (int>=0), pct (int percent, e.g., 3 for 3%).
    Output: floor(subtotal_cents * pct / 100).
    """
    return (subtotal_cents * pct) // 100


def cl29_increasing_strict(a: int, b: int, c: int) -> bool:
    """Midterm-style
    Problem: True iff a<b<c.
    Inputs: a, b, c (int)
    Output: bool.
    """
    return a < b < c


def cl30_ticket_category(age: int) -> str:
    """Midterm-style
    Problem: Categorize age.
    Inputs: age (int>=0)
    Output: 'child' (<13), 'teen' (13–17), 'adult' (18–64), 'senior' (>=65).
    """
    if age < 13:
        return 'child'
    elif age <= 17:
        return 'teen'
    elif age <= 64:
        return 'adult'
    else:
        return 'senior'


# --------------------- Tier 3: Numeric loops & scanning (31–45) ---------------------
# Focus: for/while, counters, early exit, simple arithmetic sequences; medium.

def cl31_sum_1_to_n(n: int) -> int:
    """Midterm-style
    Problem: Compute 1+2+...+n with a loop.
    Inputs: n (int>=0)
    Output: integer sum; cl31_sum_1_to_n(0) == 0.
    """
    total = 0
    for i in range(1, n+1):
        total += i
    return total


def cl32_sum_even_to_n(n: int) -> int:
    """Midterm-style
    Problem: Sum all even numbers in [0,n].
    Inputs: n (int>=0)
    Output: integer sum (0 if n<2).
    """
    total = 0
    for i in range(0, n+1, 2):
        total += i
    return total


def cl33_factorial(n: int) -> int:
    """Midterm-style
    Problem: Compute n! using a loop. Assume n>=0.
    Inputs: n (int)
    Output: int, with cl33_factorial(0) == 1.
    """
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def cl34_power(base: int, exp: int) -> int:
    """Midterm-style
    Problem: Compute base**exp using repeated multiplication.
    Inputs: base (int), exp (int>=0)
    Output: int (1 if exp==0).
    """
    result = 1
    for _ in range(exp):
        result *= base
    return result


def cl35_count_digits(n: int) -> int:
    """Midterm-style
    Problem: Count decimal digits of |n| using integer operations.
    Inputs: n (int, can be negative)
    Output: number of digits (0→1 digit).
    """
    x = abs(n)
    if x == 0:
        return 1
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count


def cl36_sum_list(nums: list[int]) -> int:
    """Midterm-style
    Problem: Sum a list of integers with a for-loop (no built-in sum()).
    Inputs: nums (list[int]) possibly empty
    Output: integer sum.
    """
    total = 0
    for num in nums:
        total += num
    return total


def cl37_count_negatives(nums: list[int]) -> int:
    """Midterm-style
    Problem: Count negative values in nums.
    Inputs: nums (list[int])
    Output: number of elements < 0.
    """
    count = 0
    for num in nums:
        if num < 0:
            count += 1
    return count


def cl38_first_even(nums: list[int]) -> int | None:
    """Midterm-style
    Problem: Return the first even element of nums or None if none.
    Inputs: nums (list[int])
    Output: int or None; must short-circuit on first match.
    """
    for num in nums:
        if num % 2 == 0:
            return num
    return None


def cl39_index_of_max(nums: list[int]) -> int | None:
    """Midterm-style
    Problem: Return the index of the first occurrence of the maximum value.
    Inputs: nums (list[int]) possibly empty
    Output: index (int) or None if empty.
    """
    if not nums:
        return None
    max_val = nums[0]
    max_idx = 0
    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            max_idx = i
    return max_idx


def cl40_fizzbuzz(n: int) -> list[str]:
    """Midterm-style
    Problem: Produce FizzBuzz from 1..n.
    Rules: 'FizzBuzz' if divisible by 3 and 5; 'Fizz' if by 3; 'Buzz' if by 5; else the number string.
    Inputs: n (int>=1)
    Output: list[str] of length n.
    """
    result = []
    for i in range(1, n+1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def cl41_sum_until_negative(nums: list[int]) -> int:
    """Midterm-style
    Problem: Sum values until you encounter a negative, then stop (do not include the negative).
    Inputs: nums (list[int])
    Output: integer sum of the prefix before first negative (or all if none negative).
    """
    total = 0
    for num in nums:
        if num < 0:
            break
        total += num
    return total


def cl42_gcd(a: int, b: int) -> int:
    """Midterm-style
    Problem: Compute the greatest common divisor via the Euclidean algorithm (loops).
    Inputs: a, b (int) possibly zero or negative. Use absolute values internally.
    Output: gcd(a,b) with gcd(0,0) defined as 0.
    """
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a


def cl43_lcm(a: int, b: int) -> int:
    """Midterm-style
    Problem: Compute least common multiple using gcd.
    Inputs: a, b (int)
    Output: nonnegative LCM (0 if either is 0). Use cl42_gcd() internally.
    """
    if a == 0 or b == 0:
        return 0
    gcd = cl42_gcd(a, b)
    return abs(a // gcd * b)


def cl44_collatz_steps(n: int) -> int:
    """Midterm-style
    Problem: Return the number of steps to reach 1 using Collatz rules:
      if n is even: n <- n//2; else: n <- 3*n+1. Count steps until n==1.
    Inputs: n (int>=1)
    Output: int steps (0 if n==1).
    """
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def cl45_primes_up_to(n: int) -> list[int]:
    """Midterm-style
    Problem: Return a list of all primes <= n using a naive primality check.
    Inputs: n (int>=2)
    Output: list of primes in ascending order. Simplicity > performance.
    """
    primes = []
    for candidate in range(2, n+1):
        is_prime = True
        for divisor in range(2, int(candidate**0.5) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
    return primes


# ------------------------ Tier 4: Strings, tuples, lists (46–60) ------------------------
# Focus: scans, building strings, simple state machines, tuple returns; medium.

def cl46_count_vowels(s: str) -> int:
    """Midterm-style
    Problem: Count how many characters in s are vowels (aeiou, case-insensitive).
    Inputs: s (str)
    Output: nonnegative int.
    """
    count = 0
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            count += 1
    return count


def cl47_remove_spaces(s: str) -> str:
    """Midterm-style
    Problem: Return a new string equal to s but without any space characters ' '.
    Inputs: s (str)
    Output: str with spaces removed; do not use str.replace().
    """
    result = ''
    for ch in s:
        if ch != ' ':
            result += ch
    return result


def cl48_reverse_string_loop(s: str) -> str:
    """Midterm-style
    Problem: Return s reversed using a loop (no slicing [::-1]).
    Inputs: s (str)
    Output: reversed string.
    """
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result


def cl49_is_palindrome(s: str) -> bool:
    """Midterm-style
    Problem: True iff s reads the same forwards and backwards (case-sensitive).
    Inputs: s (str)
    Output: bool. Implement using slicing or a loop.
    """
    return s == s[::-1]


def cl50_count_words_no_split(s: str) -> int:
    """Midterm-style
    Problem: Count words separated by single spaces WITHOUT using split(). Words are maximal
    sequences of non-space characters. Leading/trailing/multiple spaces may appear; count correctly.
    Inputs: s (str)
    Output: nonnegative int.
    """
    count = 0
    in_word = False
    for ch in s:
        if ch != ' ' and not in_word:
            count += 1
            in_word = True
        elif ch == ' ':
            in_word = False
    return count


def cl51_digit_distribution(passwords: list[str]) -> list[int]:
    """Midterm-style
    Problem: Given a list of password strings, return a length-10 list where index d is the total
    count of digit character str(d) across all passwords.
    Inputs: passwords (list[str])
    Output: list[int] of length 10. Do not use regex; use loops/conditions.
    """
    counts = [0]*10
    for pwd in passwords:
        for ch in pwd:
            if '0' <= ch <= '9':
                counts[ord(ch) - ord('0')] += 1
    return counts


def cl52_toggle_case_ascii(s: str) -> str:
    """Midterm-style
    Problem: Toggle the case of alphabetic ASCII characters without using .upper()/.lower().
    Inputs: s (str). Only 'A'..'Z' and 'a'..'z' should be toggled; other chars unchanged.
    Output: new str.
    Hint: use ord()/chr() and ASCII ranges.
    """
    result = ''
    for ch in s:
        o = ord(ch)
        if 65 <= o <= 90:
            result += chr(o + 32)
        elif 97 <= o <= 122:
            result += chr(o - 32)
        else:
            result += ch
    return result


def cl53_shift_digits_wrap(s: str, k: int) -> str:
    """Midterm-style
    Problem: Shift every decimal digit in s by k (an int in [-9,9]), wrapping within 0..9; other
    characters unchanged.
    Inputs: s (str), k (int)
    Output: new str.
    Example: ("a9b8", 2) -> "a1b0"; ("pass1", -2) -> "pass9".
    """
    result = ''
    for ch in s:
        if '0' <= ch <= '9':
            digit = (ord(ch) - ord('0') + k) % 10
            result += chr(digit + ord('0'))
        else:
            result += ch
    return result


def cl54_letters_then_digits(s: str) -> bool:
    """Midterm-style
    Problem: Return True iff s matches the pattern of one-or-more letters followed by one-or-more digits,
    and contains nothing else (no symbols). Do NOT use regex.
    Inputs: s (str)
    Output: bool.
    """
    if not s:
        return False
    i = 0
    # at least one letter
    if not s[i].isalpha():
        return False
    while i < len(s) and s[i].isalpha():
        i += 1
    if i == 0 or i == len(s):
        return False
    # at least one digit
    j = i
    while j < len(s) and s[j].isdigit():
        j += 1
    return j == len(s)


def cl55_first_index_of(s: str, ch: str) -> int | None:
    """Midterm-style
    Problem: Return index of the first occurrence of single-character ch in s, or None if absent.
    Do not use s.find()/index(). Implement with a loop.
    Inputs: s (str), ch (str of length 1)
    Output: int index or None.
    """
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return None


def cl56_run_length_encode(s: str) -> str:
    """Midterm-style
    Problem: Return a simple run-length encoding of s where each run is encoded as <char><count>.
    Singletons should include count 1. Example: 'aaabb' -> 'a3b2'; 'ab' -> 'a1b1'.
    Inputs: s (str) possibly empty
    Output: encoded str.
    """
    if not s:
        return ''
    result = ''
    current_char = s[0]
    count = 1
    for ch in s[1:]:
        if ch == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = ch
            count = 1
    result += current_char + str(count)
    return result


def cl57_all_unique_chars_no_set(s: str) -> bool:
    """Midterm-style
    Problem: Return True iff all characters in s are unique. Do NOT use set().
    Inputs: s (str)
    Output: bool. Use nested loops if needed.
    """
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def cl58_tuple_swap_xy(p: tuple[int, int]) -> tuple[int, int]:
    """Midterm-style
    Problem: Given a 2-tuple (x,y), return (y,x).
    Inputs: p (tuple[int,int])
    Output: tuple[int,int]
    """
    return (p[1], p[0])


def cl59_hms_from_seconds(total_seconds: int) -> tuple[int,int,int]:
    """Midterm-style
    Problem: Convert nonnegative total seconds into (h, m, s) with 0<=m,s<60 using // and %.
    Inputs: total_seconds (int>=0)
    Output: (hours, minutes, seconds)
    """
    h = total_seconds // 3600
    rem = total_seconds % 3600
    m = rem // 60
    s = rem % 60
    return (h, m, s)


def cl60_center_pad(s: str, width: int, pad: str = ' ') -> str:
    """Midterm-style
    Problem: Center string s in a field of given width using pad as the fill character. If the total
    padding is odd, place the extra pad on the right. If width <= len(s), return s unchanged.
    Inputs: s (str), width (int), pad (single-character str)
    Output: new str.
    """
    length = len(s)
    if width <= length:
        return s
    total_pad = width - length
    left_pad = total_pad // 2
    right_pad = total_pad - left_pad
    return pad * left_pad + s + pad * right_pad


# ------------------------ Tier 5: Lists-of-lists & tables (61–72) ------------------------
# Focus: list-of-lists scans, column ops, mutation vs copying, joins; medium→harder.

def cl61_extract_column(table: list[list], col_name: str) -> list:
    """Midterm-style
    Problem: Given a table as list-of-lists where row 0 is headers (strings), return a new list of the
    values in the named column for the remaining rows.
    Inputs: table (list[list]), col_name (str) guaranteed present among headers.
    Output: list of column values (may be empty if no data rows).
    """
    headers = table[0]
    col_index = headers.index(col_name)
    result = []
    for row in table[1:]:
        result.append(row[col_index])
    return result


def cl62_instances_in_column(table: list[list], value, col_name: str) -> int:
    """Midterm-style
    Problem: Count how many rows contain exactly `value` in the given column.
    Inputs: table (list[list]), value (any), col_name (str)
    Output: nonnegative int count.
    """
    headers = table[0]
    col_index = headers.index(col_name)
    count = 0
    for row in table[1:]:
        if row[col_index] == value:
            count += 1
    return count


def cl63_select_columns(table: list[list], cols: list[str]) -> list[list]:
    """Midterm-style
    Problem: Produce a new table with only the given columns, in the given order. Row 0 of the result
    should be the column names; subsequent rows carry extracted values.
    Inputs: table (list-of-lists, well-formed), cols (list[str] subset of headers)
    Output: new list-of-lists table (do not mutate input table).
    """
    headers = table[0]
    indices = [headers.index(c) for c in cols]
    result = [cols[:]]  # copy of cols as header
    for row in table[1:]:
        new_row = [row[i] for i in indices]
        result.append(new_row)
    return result


def cl64_column_mean(table: list[list], col_name: str) -> float:
    """Midterm-style
    Problem: Compute the mean of numeric values in a column.
    Inputs: well-formed table with numeric column `col_name`; assume at least one data row.
    Output: float mean.
    """
    headers = table[0]
    col_index = headers.index(col_name)
    total = 0.0
    count = 0
    for row in table[1:]:
        total += row[col_index]
        count += 1
    return total / count


def cl65_column_std_pop(table: list[list], col_name: str) -> float:
    """Midterm-style
    Problem: Compute the *population* standard deviation of a numeric column (σ). Formula:
        σ = sqrt( (1/N) * Σ (x_i - μ)^2 ).
    Inputs: well-formed table; assume at least one data row.
    Output: float σ. Implement sqrt via exponent **0.5 (no imports).
    """
    mean = cl64_column_mean(table, col_name)
    headers = table[0]
    col_index = headers.index(col_name)
    n = len(table) - 1
    total_sq_diff = 0.0
    for row in table[1:]:
        diff = row[col_index] - mean
        total_sq_diff += diff * diff
    variance = total_sq_diff / n
    return variance ** 0.5


def cl66_filter_exact(table: list[list], col_name: str, value) -> list[list]:
    """Midterm-style
    Problem: Return a new table containing only rows whose value in `col_name` equals `value`.
    Keep the original header row (same as input). Do not mutate input.
    Inputs: table, col_name, value
    Output: filtered table.
    """
    headers = table[0]
    col_index = headers.index(col_name)
    result = [headers[:]]
    for row in table[1:]:
        if row[col_index] == value:
            result.append(row[:])
    return result


def cl67_add_row_sum_column(table: list[list], cols: list[str], new_name: str) -> None:
    """Midterm-style
    Problem: MUTATE the given table by appending a new column named `new_name`. Each data row's value
    in this new column should be the sum of values from the listed `cols` in that row.
    Inputs: table (list-of-lists), cols (list[str]), new_name (str)
    Output: None (mutates in place). Assume numeric values and valid column names.
    """
    headers = table[0]
    indices = [headers.index(c) for c in cols]
    headers.append(new_name)
    for row in table[1:]:
        s = 0
        for i in indices:
            s += row[i]
        row.append(s)


def cl68_identify_outliers(table: list[list], col_name: str, new_name: str) -> None:
    """Midterm-style
    Problem: MUTATE the table by appending a boolean column `new_name` where a row is True if its
    value in `col_name` is more than two population standard deviations away from the column mean.
    Use results consistent with cl64/65. If there are no data rows, append header only.
    Inputs: table, col_name, new_name
    Output: None (mutates in place).
    """
    headers = table[0]
    headers.append(new_name)
    if len(table) <= 1:
        return
    mean = cl64_column_mean(table, col_name)
    std = cl65_column_std_pop(table, col_name)
    col_index = headers.index(col_name)
    for row in table[1:]:
        val = row[col_index]
        row.append(abs(val - mean) > 2 * std)


def cl69_column_join(table: list[list], cols: list[str], delim: str) -> list[str]:
    """Midterm-style
    Problem: Return a list of strings where each element is the concatenation of the row's values in
    the specified columns joined by `delim`. Do not include the header row.
    Inputs: table, cols (list[str]), delim (str)
    Output: list[str] length == number of data rows. Use str() to coerce non-strings.
    """
    headers = table[0]
    indices = [headers.index(c) for c in cols]
    result = []
    for row in table[1:]:
        items = [str(row[i]) for i in indices]
        result.append(delim.join(items))
    return result


def cl70_deep_copy_matrix(mat: list[list[int]]) -> list[list[int]]:
    """Midterm-style
    Problem: Return a deep copy of an integer matrix (list of lists). A deep copy duplicates the inner
    lists so that changing the result does not alter the original.
    Inputs: mat (list[list[int]]) possibly empty
    Output: deep-copied matrix.
    """
    result = []
    for row in mat:
        result.append(row[:])
    return result


def cl71_matrix_trace(mat: list[list[int]]) -> int:
    """Midterm-style
    Problem: Return the sum of the main diagonal of a square matrix using loops.
    Inputs: mat (n×n list-of-lists of ints); assume square and well-formed.
    Output: int trace.
    """
    total = 0
    n = len(mat)
    for i in range(n):
        total += mat[i][i]
    return total


def cl72_matrix_is_upper_triangular(mat: list[list[int]]) -> bool:
    """Midterm-style
    Problem: Return True iff all entries strictly below the main diagonal are 0.
    Inputs: mat (n×n list-of-lists of ints)
    Output: bool. Use nested loops. Do not modify the input.
    """
    n = len(mat)
    for i in range(n):
        for j in range(i):
            if mat[i][j] != 0:
                return False
    return True


# ----------------------------- Tier 6: Capstones (73–75) -----------------------------
# Focus: slightly harder integrative problems; still solvable with course tools.

def cl73_longest_run(s: str) -> tuple[str, int]:
    """Midterm-style (slightly harder)
    Problem: Find the longest run of identical consecutive characters in s.
    Inputs: s (str) possibly empty.
    Output: (char, length) for the first longest run. If s is empty, return ('', 0).
    Approach: Single left-to-right scan; maintain current run and best run.
    """
    if not s:
        return ('', 0)
    best_char = s[0]
    best_len = 1
    current_char = s[0]
    current_len = 1
    for ch in s[1:]:
        if ch == current_char:
            current_len += 1
        else:
            if current_len > best_len:
                best_len = current_len
                best_char = current_char
            current_char = ch
            current_len = 1
    if current_len > best_len:
        best_len = current_len
        best_char = current_char
    return (best_char, best_len)


def cl74_two_sum_indices(nums: list[int], target: int) -> tuple[int, int] | None:
    """Midterm-style (slightly harder)
    Problem: Return a pair of indices (i,j) with i<j such that nums[i]+nums[j]==target, or None if no
    such pair exists. Use O(n^2) nested loops (no dict/set). Return the first pair found by natural order.
    Inputs: nums (list[int]), target (int)
    Output: (i,j) or None.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def cl75_spiral_border(mat: list[list[int]]) -> list[int]:
    """Midterm-style (slightly harder)
    Problem: Return the outer border of a rectangular matrix in clockwise order starting from the
    top-left corner: go right across top row, then down rightmost column (excluding top corner), then
    left across bottom row (if distinct from top), then up leftmost column (excluding corners).
    Inputs: mat (list-of-lists of ints) with at least 1 row and 1 column; rows are equal length.
    Output: list[int] representing the border in order.
    Edge cases: Single row or single column should just return that row/column.
    """
    rows = len(mat)
    cols = len(mat[0])
    result = []

    # single row
    if rows == 1:
        return mat[0][:]

    # single column
    if cols == 1:
        return [mat[i][0] for i in range(rows)]

    # top row
    for c in range(cols):
        result.append(mat[0][c])

    # right column (excluding top)
    for r in range(1, rows):
        result.append(mat[r][cols-1])

    # bottom row (if distinct from top)
    if rows > 1:
        for c in range(cols-2, -1, -1):
            result.append(mat[rows-1][c])

    # left column (excluding corners)
    for r in range(rows-2, 0, -1):
        result.append(mat[r][0])

    return result

# End of file
