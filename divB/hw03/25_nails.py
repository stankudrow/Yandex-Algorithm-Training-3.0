#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/25/"""


# https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%2010/987.htm


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=global-statement


if __name__ == "__main__":
    size = int(input())
    memo: list[int] = [0]
    if size > 1:
        coords = sorted(map(int, input().split()))
        memo.append(coords[1] - coords[0])
        if size > 2:
            # (coords[2] - coords[1]) + (coords[1] - coords[0])
            memo.append(coords[2] - coords[0])
            for idx in range(3, size):
                memo.append(
                    min(memo[idx - 2], memo[idx - 1])
                    + coords[idx]
                    - coords[idx - 1]
                )
    print(memo[-1])
