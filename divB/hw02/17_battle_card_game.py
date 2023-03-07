#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/17/"""

# https://en.wikipedia.org/wiki/War_(card_game)

# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=simplifiable-if-expression

from collections import deque


if __name__ == "__main__":
    steps = 0
    deck0: deque = deque()
    deck1 = deque(map(int, input().split()))
    deck2 = deque(map(int, input().split()))
    draw = True
    for _ in range(int(1e6)):
        if not (deck1 and deck2):
            draw = False if deck1 or deck2 else True
            break
        first, second = deck1.popleft(), deck2.popleft()
        steps += 1
        if first == second:
            deck0.append(first)
            deck0.append(second)
        else:
            if (
                first > second and (first, second) != (9, 0)
            ) or (first, second) == (0, 9):
                deck = deck1
            if (
                first < second and (first, second) != (0, 9)
            ) or (first, second) == (9, 0):
                deck = deck2
            while deck0:
                deck.append(deck0.popleft())
            deck.append(first)
            deck.append(second)
    if draw:
        print("botva")
    else:
        winner = "first" if deck1 else "second"
        print(f"{winner} {steps}")
