#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/33/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=duplicate-code


def is_bipartite_component(
    graph: list[list[int]], vertex: int
) -> None | dict[int, int]:
    """
    Computes if the vertex has a bipatite connectivity component.

    If the vertex has such a component, it is returned as a set of nodes.
    Otherwise, None is returned.
    """

    colour: int = True
    acc: dict[int, int] = {vertex: colour}
    colour = not colour
    call_stack: list[list[int]] = [graph[vertex - 1]]
    while call_stack:
        for adjacent in reversed(call_stack[-1]):
            if adjacent not in acc:
                acc[adjacent] = colour
                colour = not colour
                call_stack.append(graph[adjacent - 1])
                break
            if acc[adjacent] != colour:
                return None
            call_stack[-1].pop()
        else:
            colour = not colour
            call_stack.pop()
    return acc


if __name__ == "__main__":
    vertices, edges = map(int, input().split())
    is_bipartite = False
    if vertices > 0:
        is_bipartite = True
        if edges > 0:
            graph: list[list[int]] = [
                [] for _ in range(vertices)
            ]
            for _ in range(edges):
                ver1, ver2 = map(int, input().split())
                graph[ver1 - 1].append(ver2)
                graph[ver2 - 1].append(ver1)
            used_vertices: set[int] = set()
            for vertex, _ in enumerate(range(vertices), 1):
                if vertex not in used_vertices:
                    component = is_bipartite_component(
                        graph, vertex
                    )
                    if component is None:
                        is_bipartite = False
                        break
                    used_vertices.update(component)
    print("YES" if is_bipartite else "NO")
