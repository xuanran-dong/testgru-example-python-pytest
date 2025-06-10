import pytest
from src.sort import bubble_sort

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([1]) == [1]

def test_bubble_sort_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_random_order():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_bubble_sort_duplicate_elements():
    assert bubble_sort([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4]

def test_bubble_sort_negative_numbers():
    assert bubble_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

def test_bubble_sort_mixed_numbers():
    assert bubble_sort([-2, 0, 3, -1, 2]) == [-2, -1, 0, 2, 3]

def test_bubble_sort_float_numbers():
    assert bubble_sort([3.14, 1.41, 2.71, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_bubble_sort_large_numbers():
    assert bubble_sort([1000000, 999999, 999998]) == [999998, 999999, 1000000]

def test_bubble_sort_none_values():
    with pytest.raises(TypeError):
        bubble_sort([1, None, 3])

def test_bubble_sort_mixed_types():
    with pytest.raises(TypeError):
        bubble_sort([1, "2", 3])

def test_bubble_sort_non_list():
    with pytest.raises(TypeError):
        bubble_sort("not a list")
