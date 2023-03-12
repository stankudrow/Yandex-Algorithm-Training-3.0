#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/34/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=duplicate-code


from typing import Any


def topological_sort(
    dag: dict[int, list[int]]
) -> None | list[int]:
    """
    Returns the topologically sorted directed acyclic graph (DAG).

    If a graph is not DAG, then None is returned.
    """
    visited: list[int] = [0] * len(dag)
    topsort: list[int] = []
    stack: list[tuple[int, list[int]]] = []
    for node in dag:
        if visited[node - 1] == 0:  # not visited
            visited[node - 1] = 1  # temporary
            stack.append((node, dag[node]))
            while stack:
                for adnode in reversed(stack[-1][1]):
                    inode = adnode - 1
                    if visited[inode] == 0:  # not visited
                        visited[inode] = 1  # temporary
                        stack.append((adnode, dag[adnode]))
                        break
                    if visited[inode] == 1:  # temp
                        # CycleError("the graph is not DAG")
                        return None
                    visited[inode] = 2  # permanent
                    stack[-1][1].pop()
                else:
                    node, _ = stack.pop()
                    visited[node - 1] = 2  # permanent
                    topsort.append(node)
    return topsort


if __name__ == "__main__":
    vertices, edges = map(int, input().split())
    nodes: Any = []
    if vertices > 0:
        if edges > 0:
            da_graph: dict[int, list[int]] = {
                node: [] for node in range(1, vertices + 1)
            }
            for _ in range(edges):
                ver1, ver2 = map(int, input().split())
                da_graph[ver1].append(ver2)
            nodes = topological_sort(da_graph)
            if nodes is None:
                nodes = [-1]
            nodes = reversed(nodes)
        else:
            nodes = range(1, vertices + 1)
    print(*nodes, sep=" ")
