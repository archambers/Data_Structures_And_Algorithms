from graph_implementations import Graph
from typing import Dict


def get_path(end: str, parent: Dict[str, str], weighted: bool=True):
    path = [end]
    vert = end
    while parent.get(vert):
        path.append(parent[vert])
        vert = parent[vert]
    return path[::-1]


def premade_graph():
    sample_graph = Graph()
    sample_graph.insert('a', 'b', 3)
    sample_graph.insert('b', 'c', 1)
    sample_graph.insert('a', 'c', 1)
    sample_graph.insert('b', 'd', 3)
    sample_graph.insert('d', 'g', 4)
    sample_graph.insert('e', 'c', 1)
    sample_graph.insert('b', 'e', 4)
    sample_graph.insert('c', 'f', 2)
    sample_graph.insert('f', 'g', 10)
    sample_graph.insert('g', 'k', 10)
    return sample_graph

# // TODO // #
# draw_graph
# create_random_graph
# check_if_connected
# check_sparseness
# all_paths
# find_cycles
# find_negative_cycles
