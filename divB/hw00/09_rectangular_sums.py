#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/9/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


def read_prefixated_matrix(
    nrows: int, ncols: int
) -> list[list[int]]:
    """Returns the matrix with prefix sums."""
    if nrows < 1 or ncols < 1:
        return [[]]
    matrix: list[list[int]] = []
    row = [
        int(item)
        for _, item in zip(range(ncols), input().split())
    ]
    for icol in range(1, cols):
        row[icol] = row[icol - 1] + row[icol]
    matrix.append(row)
    for irow in range(1, rows):
        row = [
            int(item)
            for _, item in zip(range(ncols), input().split())
        ]
        prev_colrow_val, prev_col_val = 0, 0
        for icol in range(cols):
            row[icol] = (
                matrix[irow - 1][icol]
                + prev_col_val
                + row[icol]
                - prev_colrow_val
            )
            prev_colrow_val = matrix[irow - 1][icol]
            prev_col_val = row[icol]
        matrix.append(row[:cols])
    return matrix


if __name__ == "__main__":
    rows, cols, queries = map(int, input().split())
    prefixes = read_prefixated_matrix(rows, cols)
    for _ in range(queries):
        r1, c1, r2, c2 = [
            int(item) - 1 for item in input().split()
        ]
        prev_col_val = (
            0
            if c1 - 1 < 0 or c1 - 1 < 0
            else prefixes[r2][c1 - 1]
        )
        prev_row_val = (
            0
            if r1 - 1 < 0 or r2 - 1 < 0
            else prefixes[r1 - 1][c2]
        )
        prev_colrow_val = (
            0
            if prev_col_val == 0 or prev_row_val == 0
            else prefixes[r1 - 1][c1 - 1]
        )
        print(
            prefixes[r2][c2]
            - prev_col_val
            - prev_row_val
            + prev_colrow_val
        )
