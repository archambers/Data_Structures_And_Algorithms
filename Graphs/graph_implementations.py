from collections import defaultdict


class MinimalGraph:

    def __init__(self):
        self._container = {}  # Type:Dict[str,str]

    def insert(self, origin, dest):
        if origin in self._container:
            self._container[origin].append(dest)
        else:
            self._container[origin] = [dest]

        if dest not in self._container:
                self._container[dest] = []

    def get_neighbors(self, origin):
        return self._container[origin]


class WeightedGraph:

    def __init__(self):
        self._container = {}  # Type: Dict[str,Tuple[str,int]]

    def insert(self, origin, dest, weight):
        if origin in self._container:
            self._container[origin].append((dest, weight))
        else:
            self._container[origin] = [(dest, weight)]

        if dest not in self._container:
            self._container[dest] = []

    def get_neighbors(self, origin):
        return self._container[origin]


class Graph:

    def __init__(self, weighted=True, representation='adj_list'):
        if representation == 'adj_list':
            self._container = {}
            self._representation = 'adj_list'
        if representation == 'edge_list':
            self._container = []
            self._representation = 'edge_list'

    def insert(self, origin, dest, weight=1):
        if self._representation == 'adj_list':
            if origin in self._container:
                self._container[origin].append((dest, weight))
            else:
                self._container[origin] = [(dest, weight)]

            if dest not in self._container:
                self._container[dest] = []

    def get_neighbors(self, origin):
        return self._container[origin]

    def get_vertices(self):
        return self._container.keys()

    def get_edges(self):
        edges = []
        for vertex in self.get_vertices():
            for edge in self._container[vertex]:
                edges.append(edge)
        return edges

    def convert_to_edge_list(self):
        return self.get_edges()

    def convert_to_adj_list(self, edge_list):
        adj_list = {}
        for (origin, dest), weight in edge_list:
            if origin in adj_list:
                adj_list[origin].append((dest, weight))
            else:
                adj_list[origin] = [(dest, weight)]

    def __repr__(self):
        return str(self._container)

