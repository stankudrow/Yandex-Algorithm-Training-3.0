#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/22/"""


# https://ru.algorithmica.org/cs/general-dynamic/segments/

# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


def count_hops(cells: int, max_hop: int) -> int:
    """Counts the number of hops.

    A grasshopper hops over a 1D board of `cells` amount.
    It can hop forwards 1, 2, ..., max_hop at a time.
    """
    hops = [1, 1]  # [0] - standing, [1] - a hop to the next cell
    hopcap = min(cells, max_hop)  # max capacity of a hop
    hops += [0 for _ in range(2, cells)]
    for pos in range(2, cells):
        hops[pos] = sum(
            hops[pos - hop] for hop in range(1, hopcap + 1)
        )
    return hops[-1]


if __name__ == "__main__":
    cells, max_hop = map(int, input().split())
    print(count_hops(cells, max_hop))
