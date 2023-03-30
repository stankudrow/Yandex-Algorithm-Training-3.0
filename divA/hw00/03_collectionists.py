#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45469/problems/3/"""

# pylint: disable=invalid-name


def binsearch(seq, item) -> int:
    """binsearch_iterative."""
    lind, rind = 0, len(seq) - 1
    while lind <= rind:
        mind = (lind + rind) // 2
        midelem = seq[mind]
        if midelem == item:
            return mind
        if midelem < item:
            lind = mind + 1
        else:
            rind = mind - 1
    return max(lind, rind)


if __name__ == "__main__":
    _ = input()
    nitems = sorted(map(int, set(input().split())))
    _ = input()
    kitems = list(map(int, input().split()))
    for kitem in kitems:
        print(binsearch(nitems, kitem))
