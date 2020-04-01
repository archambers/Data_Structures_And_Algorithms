from graph_tools import premade_graph, get_path
from collections import deque
from typing import List
from sys import argv


def depth_first_search_stack(graph, start, goal) -> List[str]:
    frontier = deque()
    visited = set()
    parent = {}
    frontier.append(start)
    while frontier:
        checked_vertex = frontier.pop()
        visited.add(checked_vertex)
        for vertex, weight in graph.get_neighbors(checked_vertex):
            if vertex not in visited:
                frontier.append(vertex)
                parent[vertex] = checked_vertex
            if vertex == goal:
                return get_path(goal, parent)
    return False


def depth_first_search_recursive(graph, start, goal, parent=None):
    if parent is None:
        parent = {}
    visited = set()
    visited.add(start)
    for vertex, weight in graph.get_neighbors(start):
        if vertex not in visited:
            parent[vertex] = start
            if vertex != goal:
                depth_first_search_recursive(graph, vertex, goal, parent)
    return get_path(goal, parent)


def main():
    try:
        if argv[1] == 'stack':
            print(depth_first_search_stack(premade_graph(), 'a', 'g'))
        elif argv[1] == 'recursive':
            print(depth_first_search_recursive(premade_graph(), 'a', 'g'))
    except IndexError:
        # print(depth_first_search_stack(premade_graph(), 'a', 'g'))
        print(depth_first_search_recursive(premade_graph(), 'a', 'g'))


if __name__ == '__main__':
    main()
