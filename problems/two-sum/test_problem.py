import problem

def test__01():
    test_nums = [2,7,11,15]
    test_target = 9
    actual = problem.solution(test_nums, test_target)
    expected = [0, 1]
    assert set(actual) == set(expected)

def test__02():
    test_nums = [1,2,3,4,5,6,7,8,9]
    test_target = 17
    actual = problem.solution(test_nums, test_target)
    expected = [7, 8]
    assert set(actual) == set(expected)

def test__03():
    test_nums = [1,2,3,1,2,3]
    test_target = 6
    actual = problem.solution(test_nums, test_target)
    expected = [2, 5]
    assert set(actual) == set(expected)

def test__04():
    test_nums = [3,8,22,144]
    test_target = 147
    actual = problem.solution(test_nums, test_target)
    expected = [0, 3]
    assert set(actual) == set(expected)

