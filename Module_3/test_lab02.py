from lab02 import (
    is_balanced_parentheses,
    next_greater_to_right,
    first_non_repeating,
    hot_potato,
)

assert is_balanced_parentheses("([]){}") == True
assert is_balanced_parentheses("(]") == False
assert is_balanced_parentheses("a+(b*c)-{d/e}") == True

assert next_greater_to_right([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
assert next_greater_to_right([1, 2, 3]) == [2, 3, -1]
assert next_greater_to_right([3, 2, 1]) == [-1, -1, -1]
assert next_greater_to_right([5]) == [-1]
assert next_greater_to_right([2, 2, 2]) == [-1, -1, -1]
assert next_greater_to_right([-1, 0, -2, 2]) == [0, 2, 2, -1]

assert first_non_repeating("aabc") == "a#bb"
assert first_non_repeating("aabbcc") == "a#b#c#"
assert first_non_repeating("abc") == "aaa"
assert first_non_repeating("") == ""
assert first_non_repeating("zz") == "z#"
assert first_non_repeating("abadbc") == "aabbdd"

assert hot_potato(["A", "B", "C", "D"], 2) == "A"
assert hot_potato(["A", "B", "C", "D"], 1) == "A"
assert hot_potato(["A"], 5) == "A"
assert hot_potato(["A", "B"], 2) == "B"

names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
assert hot_potato(names, 7) == "Susan"
