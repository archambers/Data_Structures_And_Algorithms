from collections import deque
from graph_tools import get_path, premade_graph


def bfs(graph, start: str, goal: str):
    visited = []
    parent = {}
    frontier = deque()
    frontier.append(start)
    while frontier:
        check = frontier.popleft()
        visited.append(check)
        for dest, weight in graph.get_neighbors(check):
            if dest not in visited:
                frontier.append(dest)
                parent[dest] = check
            if dest == goal:
                return get_path(goal, parent)
    return False


def main():
    print(bfs(premade_graph(), 'a', 'g'))


if __name__ == '__main__':
    main()
