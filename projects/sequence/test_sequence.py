from sequence import Sequence

def test__Sequence_start_value():
    start = 0
    end = 10
    expected_value = 0
    seq = Sequence(start, end)
    actual_value = seq[0]
    assert actual_value == expected_value

def test__Sequence_end_value():
    start = 0
    end = 10
    expected_value = 9
    seq = Sequence(start, end)
    actual_value = seq[9]
    assert actual_value == expected_value

def test__Sequence_mid_value():
    start = 0
    end = 10
    expected_value = 5
    seq = Sequence(start, end)
    actual_value = seq[5]
    assert actual_value == expected_value

def test__Sequence_length():
    start = 0
    end = 10
    expected_value = 10
    seq = Sequence(start, end)
    actual_value = len(seq)
    assert actual_value == expected_value

