#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45469/problems/6/"""

# pylint: disable=invalid-name

from typing import List, Tuple


def find_range(
    ranges: List[Tuple[int, int]], lim: int
) -> Tuple[int, str]:
    """Returns the index of the first range intersection."""
    left, right = 0, len(ranges) - 1
    idx = 0
    while left <= right:
        idx = (left + right) // 2
        midleft, midright = ranges[idx]
        if lim < midleft:
            right = idx - 1
            idx -= 1
        elif lim > midright:
            left = idx + 1
            idx += 1
        else:
            return (idx, "r")
    return (max(left, right), "i")


if __name__ == "__main__":
    memlim = int(input())
    sectors: List[Tuple[int, int]] = []
    for _ in range(int(input())):
        lsec, rsec = tuple(map(int, input().split()))
        lidx, lact = find_range(sectors, lsec)
        ridx, ract = find_range(sectors, rsec)
        sector = (lsec, rsec)
        if lidx == ridx:
            if lact == ract == "i":
                sectors.insert(lidx, sector)
            else:
                sectors[lidx] = sector
        else:
            if ract == "r":
                sectors[lidx : ridx + 1] = [sector]
            else:
                sectors[lidx:ridx] = [sector]
    print(len(sectors))
