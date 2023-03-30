#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45469/problems/1/"""

# pylint: disable=invalid-name

from collections import Counter
from fileinput import input as finput


def read_stdin() -> Counter:
    """Returns the chars and their frequences from stdin."""
    chars_freqs: Counter = Counter()
    for line in finput():
        chars_freqs += Counter(line.strip())
    if " " in chars_freqs:
        chars_freqs.pop(" ")
    return chars_freqs


if __name__ == "__main__":
    stats = read_stdin()
    if stats:
        STRING = "".join(sorted(stats))
        lines = []
        for _ in range(max(stats.values())):
            chars = []
            for char in STRING:
                stats[char] -= 1
                chars.append(" " if stats[char] < 0 else "#")
            lines.append("".join(chars))
        lines.reverse()
        print(*lines, sep="\n")
        print(STRING)
