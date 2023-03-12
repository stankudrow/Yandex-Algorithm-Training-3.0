#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/32/"""


# https://e-maxx.ru/algo/connected_components


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=duplicate-code


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
    components: list[set[int]] = []
    if vertices > 0:
        if edges > 0:
            graph: list[list[int]] = [
                [] for _ in range(vertices)
            ]
            for _ in range(edges):
                ver1, ver2 = map(int, input().split())
                graph[ver1 - 1].append(ver2)
                graph[ver2 - 1].append(ver1)
            used_vertices: set[int] = set()
            components = []
            for vertex, _ in enumerate(range(vertices), 1):
                if vertex not in used_vertices:
                    component = find_connectivity_component(
                        graph, vertex
                    )
                    components.append(component)
                    used_vertices.update(component)
        else:
            components = [{ver + 1} for ver in range(vertices)]
    print(len(components))
    for component in components:
        print(len(component))
        print(*component, sep=" ")
