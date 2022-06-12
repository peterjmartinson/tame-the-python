from iterable import StandardIterable
from iterable import ContainerIterable

def test__StandardIterable_start_value():
    start = 0
    end = 10
    expected_value = 0
    iterable = StandardIterable(start, end)
    actual_value = next(iterable)
    assert actual_value == expected_value

def test__StandardIterable_end_value():
    start = 0
    end = 10
    expected_value = 9
    iterable = StandardIterable(start, end)
    for i in iterable:
        actual_value = i
    assert actual_value == expected_value

def test__StandardIterable_all_values():
    start = 0
    end = 10
    expected_value = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
    iterable = StandardIterable(start, end)
    actual_value = 0
    for i in iterable:
        actual_value += i
    assert actual_value == expected_value


def test__ContainerIterable_start_value():
    start = 0
    end = 10
    expected_value = 0
    iterable = ContainerIterable(start, end)
    actual_value = next(iterable)
    assert actual_value == expected_value

def test__ContainerIterable_end_value():
    start = 0
    end = 10
    expected_value = 9
    iterable = ContainerIterable(start, end)
    for i in iterable:
        actual_value = i
    assert actual_value == expected_value

def test__ContainerIterable_all_values():
    start = 0
    end = 10
    expected_value = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
    iterable = ContainerIterable(start, end)
    actual_value = 0
    for i in iterable:
        actual_value += i
    assert actual_value == expected_value
