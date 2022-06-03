from collections import deque

class Graph:

    def __init__(self, edges, n):

        self.adjList = [[] for _ in range(n)] # adjacency list

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

    def get_list(self):
        return self.adjList


if __name__ == '__main__':

    edges = [(1,2), (1,3), (1,4), (2,5), (2,6), (5,9), (5,10), (4,7), (4,8), (7,11), (7,12)]
    nodes = 15
    graph = Graph(edges,nodes)
    print(graph.get_list())
