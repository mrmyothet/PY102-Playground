# tests/test_lab02.py
# Lab 02 — Stack & Queue (20 points total)
#
# Scoring: 4 questions × 5 points each = 20
# - Q1 is_balanced_parentheses: 5
# - Q2 next_greater_to_right:   5
# - Q3 first_non_repeating:     5
# - Q4 hot_potato:              5
#
# This test file loads the student's code from:
#   STUDENT_DIR/lab02.py
# where STUDENT_DIR is set by your runner script.

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import pytest

from lab02 import (
    is_balanced_parentheses,
    next_greater_to_right,
    first_non_repeating,
    hot_potato,
)


# def load_lab02():
#     student_dir = os.environ.get("STUDENT_DIR")
#     assert student_dir, "STUDENT_DIR env var not set"

#     lab_path = Path(student_dir) / "lab02.py"
#     assert lab_path.exists(), f"Missing file: {lab_path}"

#     spec = importlib.util.spec_from_file_location("student_lab02", lab_path)

#     assert spec and spec.loader
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)
#     return module


@pytest.mark.points(5)
def test_q1_is_balanced_parentheses():

    f = is_balanced_parentheses
    assert f("([]){}") is True
    assert f("(]") is False
    assert f("a+(b*c)-{d/e}") is True
    assert f("([)]") is False
    assert f("") is True
    assert f("(((") is False
    assert f("no brackets here!") is True


@pytest.mark.points(5)
def test_q2_next_greater_to_right():

    f = next_greater_to_right
    assert f([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert f([1, 2, 3]) == [2, 3, -1]
    assert f([3, 2, 1]) == [-1, -1, -1]
    assert f([5]) == [-1]
    assert f([2, 2, 2]) == [-1, -1, -1]
    assert f([-1, 0, -2, 2]) == [0, 2, 2, -1]


@pytest.mark.points(5)
def test_q3_first_non_repeating():

    f = first_non_repeating
    assert f("aabc") == "a#bb"
    assert f("aabbcc") == "a#b#c#"
    assert f("abc") == "aaa"
    assert f("") == ""
    assert f("zz") == "z#"
    # assert f("abadbc") == "aabbdd"


@pytest.mark.points(5)
def test_q4_hot_potato():

    f = hot_potato

    assert f(["A", "B", "C", "D"], 2) == "A"
    assert f(["A", "B", "C", "D"], 1) == "A"
    assert f(["A"], 5) == "A"
    assert f(["A", "B"], 2) == "B"

    names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    assert f(names, 7) == "Susan"


test_q1_is_balanced_parentheses()
test_q2_next_greater_to_right()
test_q3_first_non_repeating()
test_q4_hot_potato()
