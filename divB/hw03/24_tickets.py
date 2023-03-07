#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/24/"""


# https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%208/799.htm


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=global-statement


if __name__ == "__main__":
    persons = int(input())
    for_one = [0, 0, 0]
    for_two = [0, 0, 0]
    for_three = [0, 0, 0]
    for idx in range(min(3, persons)):
        for_one[idx], for_two[idx], for_three[idx] = map(
            int, input().split()
        )
    opts: list[int] = [0]
    if persons > 0:
        opts.append(for_one[0])
        if persons > 1:
            opts.append(min(for_one[0] + for_one[1], for_two[0]))
            if persons > 2:
                opts.append(
                    min(
                        for_one[2] + opts[2],
                        for_two[1] + opts[1],
                        for_three[0] + opts[0],
                    )
                )
    for pos in range(3, persons):
        one, two, three = map(int, input().split())
        for_one.append(one)
        for_two.append(two)
        for_three.append(three)
        opts.append(
            min(
                for_one[pos] + opts[pos],
                for_two[pos - 1] + opts[pos - 1],
                for_three[pos - 2] + opts[pos - 2],
            )
        )
    print(opts[-1])
