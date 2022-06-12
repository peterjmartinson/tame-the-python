from graph import Graph
from unittest import TestCase

test_list = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
test_graph = {'A': {'B'}, 'B': {'D', 'C'}, 'C': {'D'}, 'E': {'F'}, 'F': {'C'}}

def test__adjacency_to_dict():
    graph = Graph(test_list)
    expected = test_graph
    actual = graph.structure()
    TestCase().assertDictEqual(expected, actual)

def test__add_new_edge():
    graph = Graph(test_list)
    new_edge = ('G', 'H')
    graph.add_node(new_edge)
    expected = {'A': {'B'}, 'B': {'D', 'C'}, 'C': {'D'}, 'E': {'F'}, 'F': {'C'}, 'G': {'H'}}
    actual = graph.structure()
    TestCase().assertDictEqual(expected, actual)

def test__add_new_edge_old_starting_node():
    graph = Graph(test_list)
    new_edge = ('A', 'H')
    graph.add_node(new_edge)
    expected = {'A': {'B', 'H'}, 'B': {'D', 'C'}, 'C': {'D'}, 'E': {'F'}, 'F': {'C'}}
    actual = graph.structure()
    TestCase().assertDictEqual(expected, actual)

def test__add_new_edge_old_ending_node():
    graph = Graph(test_list)
    new_edge = ('H', 'A')
    graph.add_node(new_edge)
    expected = {'A': {'B'}, 'B': {'D', 'C'}, 'C': {'D'}, 'E': {'F'}, 'F': {'C'}, 'H': {'A'}}
    actual = graph.structure()
    TestCase().assertDictEqual(expected, actual)

