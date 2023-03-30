#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/37/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=duplicate-code


from collections import defaultdict, deque


def get_minpath_length(
    graph: dict[int, list[int]], _from: int, _to: int
) -> list[int]:
    """Returns the [_from, _to] path in the graph."""
    path: list[int] = []
    if (_from not in graph) or (_to not in graph):
        return path
    # child : parent
    nodes: dict[int, int] = {_from: -1}
    queue: deque[int] = deque([_from])
    while queue:
        for _ in range(len(queue)):
            for adnode in graph[queue[0]]:
                if adnode not in nodes:
                    nodes[adnode] = queue[0]
                    queue.append(adnode)
                if adnode == _to:
                    break
            else:
                queue.popleft()
                continue
            break
        else:
            continue
        node = _to
        while node != -1:
            path.append(node)
            node = nodes[node]
        break
    return path


if __name__ == "__main__":
    vertices = int(input())
    min_path: list[int] = []
    if vertices > 0:
        graph: dict[int, list[int]] = defaultdict(list)
        # an undirected graph will be given in the form of an adjacency matrix
        for rnode in range(vertices):
            nodes = [int(item) for item in input().split()]
            for cnode in range(rnode, vertices):
                quantity = nodes[cnode]
                graph[rnode + 1] += [
                    cnode + 1 for _ in range(quantity)
                ]
                if rnode != cnode:
                    graph[cnode + 1] += [
                        rnode + 1 for _ in range(quantity)
                    ]
        _from, _to = map(int, input().split())
        min_path = get_minpath_length(graph, _from, _to)
    length: int = len(min_path) - 1 if min_path else -1
    print(length)
    if length > 0:
        print(*min_path, sep=" ")
