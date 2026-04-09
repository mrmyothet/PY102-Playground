import pytest

from lab03 import insert_chaining


def test_inserts_into_correct_bucket_basic():
    table = [[], [], []]
    out = insert_chaining(table, key=5, size=3)
    assert out == [[], [], [5]]


def test_inserts_into_bucket_zero_when_divisible():
    table = [[], [], [], []]
    out = insert_chaining(table, key=8, size=4)  # 8 % 4 == 0
    assert out == [[8], [], [], []]


def test_appends_to_existing_bucket():
    table = [[], [1, 4], []]
    out = insert_chaining(table, key=7, size=3)  # 7 % 3 == 1
    assert out == [[], [1, 4, 7], []]


def test_multiple_inserts_same_bucket_preserves_order():
    table = [[], [], []]
    insert_chaining(table, key=2, size=3)  # bucket 2
    insert_chaining(table, key=5, size=3)  # bucket 2
    insert_chaining(table, key=8, size=3)  # bucket 2
    assert table == [[], [], [2, 5, 8]]


def test_collision_different_keys_same_index():
    table = [[], [], []]
    insert_chaining(table, key=1, size=3)  # 1 % 3 == 1
    insert_chaining(table, key=4, size=3)  # 4 % 3 == 1
    assert table == [[], [1, 4], []]


def test_negative_key_goes_to_python_mod_index():
    table = [[], [], []]
    out = insert_chaining(table, key=-1, size=3)  # -1 % 3 == 2 in Python
    assert out == [[], [], [-1]]


def test_zero_key_inserts_into_bucket_zero():
    table = [[], []]
    out = insert_chaining(table, key=0, size=2)
    assert out == [[0], []]


def test_returns_same_table_object_mutates_in_place():
    table = [[], [], []]
    out = insert_chaining(table, key=5, size=3)
    assert out is table  # same object returned
    assert table == [[], [], [5]]  # and it was mutated


def test_only_target_bucket_changes():
    table = [[10], [20], [30]]
    out = insert_chaining(table, key=5, size=3)  # bucket 2
    assert out[0] == [10]
    assert out[1] == [20]
    assert out[2] == [30, 5]


def test_raises_zero_division_when_size_is_zero():
    table = [[]]
    with pytest.raises(ZeroDivisionError):
        insert_chaining(table, key=1, size=0)


def test_raises_index_error_when_size_larger_than_table_len():
    # index computed with `size` can exceed table's last index if table is smaller than size
    table = [[], []]  # len(table)=2
    # key % size = 4, but table[4] will raise IndexError
    with pytest.raises(IndexError):
        insert_chaining(table, key=9, size=5)


test_inserts_into_correct_bucket_basic()
test_inserts_into_bucket_zero_when_divisible()
test_appends_to_existing_bucket()
test_multiple_inserts_same_bucket_preserves_order()
test_collision_different_keys_same_index()
test_negative_key_goes_to_python_mod_index()
test_zero_key_inserts_into_bucket_zero()
test_returns_same_table_object_mutates_in_place()
test_only_target_bucket_changes()
test_raises_zero_division_when_size_is_zero()
test_raises_index_error_when_size_larger_than_table_len()
