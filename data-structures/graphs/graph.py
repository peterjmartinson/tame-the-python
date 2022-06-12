

class Graph:

    def __init__(self, adjacency_list=None):
        self.graph = {}
        self.build_graph_from_adjacency_list(adjacency_list)

    def structure(self):
        return self.graph

    def build_graph_from_adjacency_list(self, adjacency_list):
        # for node1, node2 in adjacency_list:
        for node_tuple in adjacency_list:
            self.add_node(node_tuple)
            # if str(node1) in self.graph.keys():
            #     self.graph[str(node1)].add(str(node2))
            # else:
            #     self.graph[str(node1)] = {str(node2)}

    def add_node(self, node_tuple):
        node1 = node_tuple[0]
        node2 = node_tuple[1]
        if str(node1) in self.graph.keys():
            self.graph[str(node1)].add(str(node2))
        else:
            self.graph[str(node1)] = {str(node2)}




