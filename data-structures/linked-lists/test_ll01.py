from ll01 import Node, LinkedList

class TestNode:

    def test__build_node_data(self):
        test_val = 3
        node = Node(test_val)
        expected = test_val
        actual = node.data
        assert expected == actual

    def test__build_node_next(self):
        test_val = 3
        node = Node(test_val)
        expected = None
        actual = node.next
        assert expected == actual

class TestLinkedList:

    def test__build_linked_list_head(self):
        ll = LinkedList()
        expected = None
        actual = ll.head
        assert expected == actual

    def test__build_linked_list_outputs_nodes(self):
        ll = LinkedList()
        a = Node("a")
        b = Node("b")
        c = Node("c")
        ll.head = a
        a.next = b
        b.next = c
        expected = "a -> b -> c -> None"
        actual = str(ll)
        assert expected == actual

    def test__build_linked_list_from_list(self):
        nodes = ["a", "b", "c"]
        ll = LinkedList(nodes=nodes)
        expected = "a -> b -> c -> None"
        actual = str(ll)
        assert expected == actual

    def test__iteration(self):
        ll = LinkedList()
        a = Node("a")
        b = Node("b")
        c = Node("c")
        ll.head = a
        a.next = b
        b.next = c
        test_list = []
        for i in ll:
            test_list.append(i)
        expected = "b"
        actual = str(test_list[1])
        assert expected == actual

    def test__add_new_head(self):
        ll = LinkedList()
        a = Node("a")
        b = Node("b")
        c = Node("c")
        ll.head = a
        a.next = b
        b.next = c
        d = Node("d")
        ll.add_first(d)
        expected = d
        actual = ll.head
        assert expected == actual

    def test__add_new_tail(self):
        ll = LinkedList()
        a = Node("a")
        b = Node("b")
        c = Node("c")
        ll.head = a
        a.next = b
        b.next = c
        d = Node("d")
        ll.add_last(d)
        expected = d
        node = ll.head
        while node.next:
            node = node.next
        actual = node
        assert expected == actual
    
    def test__getitem(self):
        ll = LinkedList()
        a = Node("a")
        b = Node("b")
        c = Node("c")
        ll.head = a
        a.next = b
        b.next = c
        expected = a
        actual = ll[0]
        assert expected == actual

    def test__getitem(self):
        ll = LinkedList()
        a = Node("a")
        b = Node("b")
        c = Node("c")
        ll.head = a
        a.next = b
        b.next = c
        expected = b
        actual = ll[1]
        assert expected == actual

    def test__getitem(self):
        ll = LinkedList()
        a = Node("a")
        b = Node("b")
        c = Node("c")
        ll.head = a
        a.next = b
        b.next = c
        expected = b
        actual = ll[3]
        assert expected == actual



