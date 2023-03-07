#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/14/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


from typing import List


def is_order_safe(cars: List) -> bool:
    """Returns True if the sequence saves the order when being rearranged."""
    stk2: List = []
    deadlock: List = []
    for car in cars:
        while deadlock and deadlock[-1] <= car:
            top = deadlock.pop()
            if stk2 and top < stk2[-1]:
                return False
            stk2.append(top)
        deadlock.append(car)
    for _ in range(len(deadlock)):
        if stk2:
            if deadlock[-1] < stk2[-1]:
                return False
        stk2.append(deadlock.pop())
    return bool(stk2) and not deadlock


if __name__ == "__main__":
    _ = input()  # the num of cars
    cars = list(map(int, input().split()))
    print("YES" if is_order_safe(cars) else "NO")
