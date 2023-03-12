#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/35/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=duplicate-code
# pylint: disable=too-many-nested-blocks


from collections import defaultdict


def find_loop(graph: dict[int, list[int]]) -> list[int]:
    """Returns the list of nodes if the latter form a loop/cycle."""

    visited: list[int] = [0] * len(graph)
    for node in graph:
        if visited[node - 1] == 0:
            path: list[int] = [node]
            visited[node - 1] = 1
            stack: list[tuple[None | int, int, list[int]]] = [
                (None, node, graph[node])
            ]
            while stack:
                parent, source, adjacents = stack[-1]
                while adjacents:
                    adnode = adjacents.pop()
                    inode = adnode - 1
                    if visited[inode] == 0:
                        visited[inode] = 1
                        path.append(adnode)
                        stack.append(
                            (source, adnode, graph[adnode])
                        )
                        break
                    if adnode != parent:
                        cycle: list[int] = []
                        while path and path[-1] != adnode:
                            cycle.append(path.pop())
                        if path:
                            cycle.append(path.pop())
                        return cycle
                else:
                    path.pop()
                    stack.pop()
    return []


if __name__ == "__main__":
    vertices = int(input())
    loop: list[int] = []
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
        loop = find_loop(graph)
    if loop:
        print("YES")
        print(len(loop))
        print(*loop, sep=" ")
    else:
        print("NO")
