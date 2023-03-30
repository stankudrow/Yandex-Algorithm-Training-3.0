#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/10/"""


# pylint: disable=invalid-name


from collections import defaultdict


if __name__ == "__main__":
    string = input()
    length = len(string)
    freqs: dict[str, int] = defaultdict(int)
    for idx in range(length):
        freqs[string[idx]] += (idx + 1) * (length - idx)
    print(
        *[f"{char}: {freqs[char]}" for char in sorted(freqs)],
        sep="\n",
    )
