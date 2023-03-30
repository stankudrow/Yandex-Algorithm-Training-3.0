#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/8/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    size = int(input())
    # if size: ...
    xmin, ymin = map(int, input().split())
    xmax, ymax = xmin, ymin
    for _ in range(size - 1):
        xcoord, ycoord = map(int, input().split())
        xmin = min(xmin, xcoord)
        xmax = max(xmax, xcoord)
        ymin = min(ymin, ycoord)
        ymax = max(ymax, ycoord)
    print(" ".join(map(str, (xmin, ymin, xmax, ymax))))
