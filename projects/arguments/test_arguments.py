from arguments import *

def test__canary():
        assert 1 == 1

def test__positional_parameter():
    test_a = 1
    test_b = 2
    expected_value = 3
    actual_value = positional_parameter_add(test_a, test_b)
    assert actual_value == expected_value

def test__many_positional_01():
    test_a = 1
    test_b = 2
    expected_value = 3
    actual_value = many_positional_parameters_add(test_a, test_b)
    assert actual_value == expected_value

def test__many_positional_02():
    test_a = 1
    test_b = 2
    test_c = 3
    test_d = 4
    expected_value = 10
    actual_value = many_positional_parameters_add(test_a, test_b, test_c, test_d)
    assert actual_value == expected_value

def test__positional_mix_01():
    test_a = 1
    test_b = 2
    test_c = 3
    test_d = 4
    expected_value = 10
    actual_value = positional_mix_add(test_a, test_b, test_c, test_d)
    assert actual_value == expected_value

def test__positional_mix_02():
    test_a = 1
    test_b = 2
    expected_value = 3
    actual_value = positional_mix_add(test_a, test_b)
    assert actual_value == expected_value

def test__positional_mix_02():
    test_a = 1
    test_b = 2
    expected_value = 3
    actual_value = positional_mix_add(test_a, test_b)
    assert actual_value == expected_value

def test__keyword_parameter_01():
    expected_value = 0
    actual_value = keyword_parameter_add()
    assert actual_value == expected_value

def test__keyword_parameter_02():
    test_a = 1
    expected_value = 1
    actual_value = keyword_parameter_add(a=test_a)
    assert actual_value == expected_value

def test__keyword_parameter_03():
    test_b = 1
    expected_value = 1
    actual_value = keyword_parameter_add(b=test_b)
    assert actual_value == expected_value

def test__keyword_parameter_04():
    test_a = 1
    test_b = 1
    expected_value = 2
    actual_value = keyword_parameter_add(a=test_a, b=test_b)
    assert actual_value == expected_value

def test__many_keywords_01():
    test_a = 1
    test_b = 1
    expected_value = 2
    actual_value = many_keyword_parameters_add(a=test_a, b=test_b)
    assert actual_value == expected_value


