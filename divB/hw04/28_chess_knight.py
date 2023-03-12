#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/28/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    rows, cols = map(int, input().split())
    memo = [[0 for _ in range(cols)] for _ in range(rows)]
    moves = -1
    if rows > 0 and cols > 0:
        for srow, scol in zip(
            range(0, rows, 2), range(0, cols, 1)
        ):
            memo[srow][scol] += 1
            for irow, icol in zip(
                range(srow + 1, rows),
                range(scol + 2, cols, 2),
            ):
                prev1 = (
                    memo[irow - 2][icol - 1]
                    if irow - 2 > -1 and icol - 1 > -1
                    else 0
                )
                prev2 = (
                    memo[irow - 1][icol - 2]
                    if irow - 1 > -1 and icol - 2 > -1
                    else 0
                )
                memo[irow][icol] = (
                    prev1 + prev2 if prev1 and prev2 else 1
                )
        moves = memo[-1][-1]
    print(moves)
