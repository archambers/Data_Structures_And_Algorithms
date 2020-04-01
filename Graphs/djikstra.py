from graph_tools import get_path, premade_graph
from heapq import heappop, heapify, heappush


def djikstra(graph, start, goal):
    all_nodes = graph._container.keys()
    distances = {node: float('inf') for node in all_nodes}
    distances[start] = 0
    processed = set()
    node = start
    parent = {}
    while all_nodes - processed:
        processed.add(node)  # add node to set 'processed'
        for vertex, weight in graph.get_neighbors(node):
            # check if weight in distances dictionary is larger than this path
            if vertex not in processed:
                if distances[vertex] > distances[node] + weight:
                    distances[vertex] = distances[node] + weight
                    parent[vertex] = node
        if all_nodes - processed:  # gives set of all unprocessed nodes
            # sets variable 'node' to smallest remaining unprocessed node
            node = min([i for i in all_nodes - processed],
                       key=lambda x: distances[x])
    return get_path(goal, parent)


# // TODO:
# Implement with priority queue instead of min


def djikstra_heap(graph, start, goal):
    all_nodes = graph._container.keys()
    distances = {node: float('inf') for node in all_nodes}
    distances[start] = 0
    to_explore = [(distances[start], start)]
    parent = {}
    while to_explore:
        origin_wt, origin = heappop(to_explore)
        for vertex, weight in graph.get_neighbors(origin):
            if distances[vertex] > origin_wt + weight:
                distances[vertex] = origin_wt + weight
                heappush(to_explore, (origin_wt + weight, vertex))
                parent[vertex] = origin

    return get_path(goal, parent)


def main():
    sample_graph = premade_graph()
    print(djikstra_heap(sample_graph, 'a', 'g'))


if __name__ == '__main__':
    main()
