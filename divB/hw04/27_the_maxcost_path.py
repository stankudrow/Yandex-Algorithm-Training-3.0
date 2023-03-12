#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/27/"""


# pylint: disable=invalid-name
# pylint: disable=duplicate-code


if __name__ == "__main__":
    rows, cols = map(int, input().split())
    minpath = -1
    if rows > 0 and cols > 0:
        table = [
            list(map(int, input().split())) for _ in range(rows)
        ]
        turns: list[str] = []
        memo = [[0 for _ in range(cols)] for _ in range(rows)]
        memo[0][0] = table[0][0]
        for col in range(1, cols):
            memo[0][col] = memo[0][col - 1] + table[0][col]
        for row in range(1, rows):
            memo[row][0] = memo[row - 1][0] + table[row][0]
        for down in range(1, rows):
            for right in range(1, cols):
                memo[down][right] = (
                    max(
                        memo[down][right - 1],
                        memo[down - 1][right],
                    )
                    + table[down][right]
                )
        minpath = memo[-1][-1]
        up, left = rows - 1, cols - 1
        while up > 0 or left > 0:
            upval = memo[up - 1][left] if up - 1 > -1 else -1
            leftval = memo[up][left - 1] if left - 1 > -1 else -1
            if upval > leftval:
                turns.append("D")
                up -= 1
            else:
                turns.append("R")
                left -= 1
    print(minpath)
    print(*turns[::-1], sep=" ")
