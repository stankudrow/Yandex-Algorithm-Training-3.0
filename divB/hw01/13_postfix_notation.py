#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/13/"""

# pylint: disable=invalid-name


from operator import add, sub, mul
from typing import List, Union


OPS = {
    "+": add,
    "-": sub,
    "*": mul,
}


if __name__ == "__main__":
    stack: List[Union[int, str]] = []
    for token in input().split():
        op = OPS.get(token)
        if op is None:
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(op(a, b))
    print(stack.pop())
