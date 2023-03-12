#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/30/"""


# https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%2017/1618.htm


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


def get_the_levenshtein_distances(
    seq1: list, seq2: list
) -> list[list[int]]:
    """Returns the Levenshtein's distances for two sequences.

    References
    ----------
    https://en.wikipedia.org/wiki/Levenshtein_distance
    """
    size1, size2 = map(len, (seq1, seq2))
    _memo: list[list[int]] = [
        [0 for _ in range(size2 + 1)] for _ in range(size1 + 1)
    ]
    for ch1 in range(1, size1 + 1):
        for ch2 in range(1, size2 + 1):
            if seq1[ch1 - 1] == seq2[ch2 - 1]:
                res = _memo[ch1 - 1][ch2 - 1] + 1
            else:
                res = max(
                    _memo[ch1 - 1][ch2], _memo[ch1][ch2 - 1]
                )
            _memo[ch1][ch2] = res
    return _memo


if __name__ == "__main__":
    size1 = int(input())
    seq1: list[int] = list(map(int, input().split()))
    size2 = int(input())
    seq2: list[int] = list(map(int, input().split()))
    memo = get_the_levenshtein_distances(seq1, seq2)
    subseq: list[int] = []
    # print(memo)
    if size1 and size2:
        irow, icol = size1, size2
        last: int = memo[irow][icol]
        while irow and icol:
            left = memo[irow][icol - 1]
            top = memo[irow - 1][icol]
            if last == top:
                irow -= 1
            elif last == left:
                icol -= 1
            else:
                subseq.append(seq1[irow - 1])
                irow, icol = irow - 1, icol - 1
            last = memo[irow][icol]
    print(*reversed(subseq))  # just as in examples
