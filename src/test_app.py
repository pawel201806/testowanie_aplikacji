from app import (
    sort_ascending,
    sort_descending,
    remove_duplicates,
    is_sorted,
    get_numbers
)


def test_sort_ascending():
    assert sort_ascending([4, 1, 3, 2]) == [1, 2, 3, 4]
    assert sort_ascending([5, 5, 2, 1]) == [1, 2, 5, 5]
    assert sort_ascending([]) == []


def test_sort_descending():
    assert sort_descending([4, 1, 3, 2]) == [4, 3, 2, 1]
    assert sort_descending([5, 5, 2, 1]) == [5, 5, 2, 1]
    assert sort_descending([]) == []


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates([5, 5, 5]) == [5]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_is_sorted():
    assert is_sorted([1, 2, 3, 4]) == True
    assert is_sorted([1, 1, 2, 3]) == True
    assert is_sorted([4, 3, 2, 1]) == False
    assert is_sorted([]) == True
    assert is_sorted([5]) == True


def test_get_numbers(monkeypatch):
    inputs = iter(["1", "2", "3", "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert get_numbers() == [1, 2, 3]


def test_get_numbers_with_floats(monkeypatch):
    inputs = iter(["1.5", "2.5", "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert get_numbers() == [1.5, 2.5]


def test_get_numbers_with_invalid_input(monkeypatch):
    inputs = iter(["abc", "10", "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert get_numbers() == [10]


def test_get_numbers_empty(monkeypatch):
    inputs = iter(["stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert get_numbers() == []