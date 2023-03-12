#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/31/"""


# https://e-maxx.ru/algo/connected_components


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


def find_connectivity_component(
    graph: list[list[int]], vertex: int
) -> set[int]:
    """Returns the set of nodes forming the connectivity component."""

    acc: set[int] = {vertex}
    call_stack: list[list[int]] = [graph[vertex - 1]]
    while call_stack:
        for adjacent in reversed(call_stack[-1]):
            if adjacent not in acc:
                acc.update({adjacent})
                call_stack.append(graph[adjacent - 1])
                break
            call_stack[-1].pop()
        else:
            call_stack.pop()
    return acc


if __name__ == "__main__":
    vertices, edges = map(int, input().split())
    component = set()
    if vertices > 0:
        component = {1}
        if edges > 0:
            # task-specific
            graph: list[list[int]] = [
                [] for _ in range(vertices)
            ]
            for _ in range(edges):
                ver1, ver2 = map(int, input().split())
                graph[ver1 - 1].append(ver2)
                graph[ver2 - 1].append(ver1)
            if graph[0]:  # 1 - 1
                component = find_connectivity_component(graph, 1)
    print(len(component))
    print(*sorted(component), sep=" ")
