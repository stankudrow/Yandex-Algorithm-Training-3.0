#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/21/"""


# https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%203/263.htm

# pylint: disable=invalid-name
# pylint: disable=global-statement


MEMO = [2, 4, 7]


def count_no_three_ones(nbr: int) -> int:
    """Counts the sequences where is no three ones in a row."""
    if nbr < 0:
        return -1
    if nbr < 1:
        return 0
    global MEMO
    start = len(MEMO)
    MEMO += [0 for _ in range(start, nbr)]
    for pos in range(start, nbr):
        MEMO[pos] = MEMO[pos - 1] + MEMO[pos - 2] + MEMO[pos - 3]
    return MEMO[nbr - 1]


if __name__ == "__main__":
    num = int(input())
    print(count_no_three_ones(num))
