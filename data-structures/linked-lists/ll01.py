# https://realpython.com/linked-lists-python/
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            for n in nodes:
                node.next = Node(data=n)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node:
            yield node  # note, this yields Node()s, not node.data
            node = node.next

    def __getitem__(self, key):
        if key == 0:
            return self.head
        node = self.head
        for i in range(1,key+1):
            node = node.next
        raise IndexError('LinkedList index out of range')
        return node


    def add_first(self, node) -> None:
        node.next = self.head
        self.head = node

    def add_last(self, node) -> None:
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


if __name__ == "__main__":
    ll = LinkedList()

    first_node = Node("a")
    ll.head = first_node  # here, note that the LinkedList is really just a copy of the first node.

    second_node = Node("b")
    third_node = Node("c")
    first_node.next = second_node
    second_node.next = third_node

    print(list(ll)[1])
