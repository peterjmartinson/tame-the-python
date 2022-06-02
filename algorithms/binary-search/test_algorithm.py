from algorithm import *
import numpy as np
import random

def test__typical_01():
    input_list = [1,2,3,4,5,6,7,8,9]
    target     = 4
    expected   = 3
    result     = search(input_list, target)
    assert result == expected

def test__typical_02():
    input_list = [1,2,3,4,5,6,7,8,9]
    target     = 10
    expected   = None
    result     = search(input_list, target)
    assert result == expected

def test__typical_03():
    input_list = [1,2,3,4,5,6,7,8,9]
    target     = -5
    expected   = None
    result     = search(input_list, target)
    assert result == expected

def test__edge_zero_element():
    input_list = []
    target     = 1
    expected   = None
    result     = search(input_list, target)
    assert result == expected

def test__edge_one_element():
    input_list = [1]
    target     = 1
    expected   = 0
    result     = search(input_list, target)
    assert result == expected

def test__edge_one_element():
    input_list = [1]
    target     = 2
    expected   = None
    result     = search(input_list, target)
    assert result == expected

def test__edge_identical_elements():
    input_list = [1, 1, 1, 1, 1, 1]
    target     = 1
    expected   = None
    result     = search(input_list, target)
    assert result != expected

