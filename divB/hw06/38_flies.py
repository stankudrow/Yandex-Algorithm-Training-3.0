#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/38/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


from collections import deque


def get_next_moves(
    graph: list[list[int]],
    rows: int,
    cols: int,
    row: int,
    col: int,
) -> list[tuple[int, int]]:
    """The possible moves of a chess knight from a cell."""

    moves: list[tuple[int, int]] = []
    for irow, icol in [
        (row - 2, col - 1),
        (row - 2, col + 1),
        (row - 1, col + 2),
        (row + 1, col + 2),
        (row + 2, col - 1),
        (row + 2, col + 1),
        (row - 1, col - 2),
        (row + 1, col - 2),
    ]:
        if -1 < irow < rows and -1 < icol < cols:
            if graph[irow][icol] in (-1, 0):
                moves.append((irow, icol))
    return moves


if __name__ == "__main__":
    rows, cols, yend, xend, nflies = map(int, input().split())
    yend, xend = yend - 1, xend - 1
    total_length = -1
    if rows and cols and (-1 < yend < rows and -1 < xend < cols):
        board = [[0 for _ in range(cols)] for _ in range(rows)]
        for _ in range(nflies):
            ycoord, xcoord = [
                int(coord) - 1 for coord in input().split()
            ]
            board[ycoord][xcoord] = -1  # a fly
        if board[yend][xend] == -1:
            nflies -= 1
        board[yend][xend] = -2  # the end is marked
        nodes = deque([(yend, xend)])
        total_length, jumps = 0, 1
        while nodes:
            for _ in range(len(nodes)):
                next_moves = get_next_moves(
                    board, rows, cols, nodes[0][0], nodes[0][1]
                )
                if next_moves:
                    for yc, xc in next_moves:
                        if board[yc][xc] == -1:
                            nflies -= 1
                            total_length += jumps
                        nodes.append((yc, xc))
                        board[yc][xc] = jumps
                nodes.popleft()
            jumps += 1
        total_length = -1 if nflies else total_length
    print(total_length)
