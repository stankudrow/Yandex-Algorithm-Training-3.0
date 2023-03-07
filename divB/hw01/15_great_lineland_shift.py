#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/15/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


from typing import List


if __name__ == "__main__":
    _ = input()
    costs = [int(cost) for cost in input().split()]
    stk: List = []
    for index, cost in enumerate(costs):
        while stk and cost < stk[-1][1]:
            idx, cst = stk.pop()
            costs[idx] = index
        stk.append((index, cost))
    for index, cost in stk:
        costs[index] = -1
    print(*costs, sep=" ")
