#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/23/"""


# https://ru.algorithmica.org/cs/general-dynamic/segments/
# https://python.su/forum/topic/40754/?page=1#post-218567

# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=global-statement


NOPS = [-1, 0, 1, 1, 2]
# 0 -> 1 = -1 ops (illegal)
# -1 operation was added to make numbers and indices the same
# 1 -> 1 = 0 ops
# 1 -> 2 = 1 op (1 + 1 or 1 * 2)
# 1 -> 3 = 1 op (1 * 3)
# 1 -> 4 = 2 ops (1 * 2 * 2 or 1 * 3 + 1)


def calculate(number: int) -> tuple[int, list[int]]:
    """Calculates the optimal path from 1 to nbr.

    Available operations:
    1. X + 1
    2. X * 2
    3. X * 3

    Parameters
    ----------
    number : int, the number to reach starting with 1

    Returns
    -------
    the minimum number of operations to reach `nbr` from 1
    the list of integers got from the optimal path of operations taken.
    """
    if number < 1:
        return (-1, [-1])
    global NOPS
    start = len(NOPS)
    NOPS += [0 for _ in range(start, number + 1)]
    for num in range(start, number + 1):
        minop = NOPS[num - 1]
        if num % 3 == 0:
            minop = min(minop, NOPS[num // 3])
        if num % 2 == 0:
            minop = min(minop, NOPS[num // 2])
        NOPS[num] = minop + 1  # +1 current operation
    nbr = number
    ops = [nbr]
    while nbr > 1:
        nops = NOPS[nbr]
        if nops == (NOPS[nbr - 1] + 1):
            nbr -= 1
        elif nbr % 2 == 0 and (nops == NOPS[nbr // 2] + 1):
            nbr //= 2
        else:
            nbr //= 3
        ops.append(nbr)
    return (NOPS[number], ops[::-1])


if __name__ == "__main__":
    nbr = int(input())
    min_ops, numbers = calculate(nbr)
    print(min_ops)
    print(*numbers, sep=" ")
