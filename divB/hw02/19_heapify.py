#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/19/"""

# https://docs.python.org/3/library/heapq.html
# https://github.com/python/cpython/blob/3.11/Lib/heapq.py

# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


from typing import List


def _siftdown_max(heap: List, index: int):
    """Sifts down the maximum nodes from the index."""

    size = len(heap)
    child = 2 * index + 1  # the leftmost child
    while child < size:
        right = child + 1
        if right < size and heap[right] >= heap[child]:
            child = right
        if heap[child] <= heap[index]:
            break
        heap[index], heap[child] = heap[child], heap[index]
        index = child
        child = 2 * index + 1


def _siftup_max(heap: List, index: int):
    """Sifts up the maximum nodes from the index."""
    parent = (index - 1) // 2
    while index > 0 and heap[parent] < heap[index]:
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent
        parent = (index - 1) // 2


def heappush_max(heap: List, item):
    """Pushes the item into a max heap."""

    heap.append(item)
    _siftup_max(heap, len(heap) - 1)


def heappop_max(heap: List):
    """Pops the maximum item from a max heap."""

    last = heap.pop()
    if heap:
        retval = heap[0]
        heap[0] = last
        _siftdown_max(heap, 0)
        return retval
    return last


if __name__ == "__main__":
    maxheap: List = []
    for _ in range(int(input())):
        cmd = [int(item) for item in input().split()]
        match cmd[0]:
            case 0:
                heappush_max(maxheap, cmd[1])
            case 1:
                print(heappop_max(maxheap))
            case _:
                print(f"invalid command '{cmd[0]}'")
