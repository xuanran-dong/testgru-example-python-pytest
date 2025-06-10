import pytest
from src.sort import bubble_sort

def test_empty_list():
    assert bubble_sort([]) == []

def test_single_element():
    assert bubble_sort([1]) == [1]

def test_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_unsorted_list():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_duplicate_elements():
    assert bubble_sort([4, 4, 4, 4]) == [4, 4, 4, 4]

def test_negative_numbers():
    assert bubble_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

def test_mixed_numbers():
    assert bubble_sort([-2, 3, 0, -1, 4]) == [-2, -1, 0, 3, 4]

def test_float_numbers():
    assert bubble_sort([3.14, 1.41, 2.71, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_large_list():
    input_list = list(range(1000, 0, -1))
    expected = list(range(1, 1001))
    assert bubble_sort(input_list) == expected

def test_list_with_zero():
    assert bubble_sort([0, 1, 0, 2, 0]) == [0, 0, 0, 1, 2]

def test_list_with_strings():
    # Since bubble sort implementation doesn't explicitly check for non-numeric types,
    # we'll test if it can handle string comparison
    assert bubble_sort(['c', 'a', 'b']) == ['a', 'b', 'c']

def test_none_input():
    with pytest.raises(TypeError):
        bubble_sort(None)

def test_non_list_input():
    with pytest.raises(TypeError):
        bubble_sort(123)

def test_mixed_types():
    with pytest.raises(TypeError):
        bubble_sort([1, 'a', 2.5])
