#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/20/"""

# https://docs.python.org/3/library/heapq.html

# pylint: disable=invalid-name
# pylint: disable=duplicate-code


from typing import List


def _siftdown_min(heap: List, index: int):
    """Sifts down the minimum nodes from the index."""

    size = len(heap)
    child = 2 * index + 1  # the leftmost child
    while child < size:
        right = child + 1
        if right < size and heap[right] <= heap[child]:
            child = right
        if heap[child] >= heap[index]:
            break
        heap[index], heap[child] = heap[child], heap[index]
        index = child
        child = 2 * index + 1


def _siftup_min(heap: List, index: int):
    """Sifts up the minimum nodes from the index."""
    parent = (index - 1) // 2
    while index > 0 and heap[parent] > heap[index]:
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent
        parent = (index - 1) // 2


def heappush_min(heap: List, item):
    """Pushes the item into a min heap."""

    heap.append(item)
    _siftup_min(heap, len(heap) - 1)


def heappop_min(heap: List):
    """Pops the maximum item from a max heap."""

    last = heap.pop()
    if heap:
        retval = heap[0]
        heap[0] = last
        _siftdown_min(heap, 0)
        return retval
    return last


def heap_sort(iterable):
    """https://docs.python.org/3/library/heapq.html"""
    heap = []
    for value in iterable:
        heappush_min(heap, value)
    return [heappop_min(heap) for _ in range(len(heap))]


if __name__ == "__main__":
    _ = input()
    print(*heap_sort(map(int, input().split())))
