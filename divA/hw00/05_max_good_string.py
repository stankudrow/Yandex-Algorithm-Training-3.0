#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45469/problems/5/"""

# pylint: disable=invalid-name

from typing import List, Sequence


def squeeze(seq: List, delims: Sequence) -> List[List]:
    """Returns the collections of adjacent elements."""
    splitted = []
    while seq:
        partition = []
        amount = 0
        while seq:
            item = seq.pop()
            if item in delims:
                break
            amount += 1
            partition.append(item)
        if amount > 1:
            partition.reverse()
            splitted.append(partition)
    splitted.reverse()
    return splitted


if __name__ == "__main__":
    parts = [[int(input()) for _ in range(int(input()))]]
    good_counts = 0
    while parts:
        new_parts = []
        for part in parts:
            minfreq = min(part)
            size = len(part)
            part = [freq - minfreq for freq in part]
            new_parts += squeeze(part, [0])
            good_counts += (size - 1) * minfreq
        parts = new_parts
    print(good_counts)
