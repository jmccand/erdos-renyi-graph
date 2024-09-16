import random
from queue import Queue
# import json

class Graph:

    def __init__(self, n, p):
        # initialize adjancency list
        self.adjacency_list = {node: set() for node in range(n)}
        for node in range(n):
            # create edges
            for dest in range(node):
                if random.random() < p:
                    self.adjacency_list[node].add(dest)
                    self.adjacency_list[dest].add(node)
        # print(json.dumps({node: list(edges) for node, edges in self.adjacency_list.items()}))

    def t_component(self, t):
        full_marked = set()
        for node in self.adjacency_list.keys():
            if not node in full_marked:
                result, marked = self.breadth_first_search(t, node)
                if result:
                    return True
                full_marked.update(marked)
        return False

    def breadth_first_search(self, t, start_node):
        marked = set()
        component_size = 0
        nodes = Queue()
        nodes.put(start_node)
        while nodes.qsize() > 0:
            node = nodes.get()
            if node in marked:
                # skip node if marked already
                continue
            # add all neighbors
            for n in self.adjacency_list[node]:
                nodes.put(n)
            # mark this node and increment size
            marked.add(node)
            component_size += 1
            if component_size >= t:
                return True, marked
        return False, marked