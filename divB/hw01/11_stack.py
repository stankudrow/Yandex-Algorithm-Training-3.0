#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/11/"""

# pylint: disable=invalid-name


from typing import Any, Optional, Sequence


class StackError(Exception):
    """Generic Stack Exception."""


class Stack:
    """The Stack data structure."""

    def __init__(
        self,
        seq: Optional[Sequence] = None,
        maxlen: Optional[int] = None,
    ):
        if seq is None:
            self._stack = []
        else:  # mypy
            self._stack = list(seq)
        if maxlen and maxlen < 0:
            raise StackError(f"maxlen (={maxlen}) < 0")
        self._maxlen = maxlen

    def __bool__(self) -> bool:
        return bool(self._stack)

    def __len__(self) -> int:
        return len(self._stack)

    def __repr__(self) -> str:
        return f"Stack({self._stack})"

    def clear(self):
        """Clears the stack, making it empty."""
        self._stack.clear()

    def is_empty(self) -> bool:
        """Returns True if the stack is empty."""
        return not bool(self)

    def extend(self, seq: Sequence):
        """Pushes the elements from the sequence."""
        lst = list(seq)
        if self.maxlen is None:
            cap = len(lst)
        else:
            cap = min(len(lst), self.maxlen - len(self))
        for idx in range(cap):
            self._stack.append(lst[idx])

    def pop(self) -> Any:
        """Pops the last/top element.

        Raises
        ------
        IndexError
            if empty.
        """
        return self._stack.pop()

    def push(self, value: Any):
        """Pushes the value onto the stack."""
        if self.maxlen is None or (
            (self.maxlen is not None) and len(self) < self.maxlen
        ):
            self._stack.append(value)

    @property
    def maxlen(self) -> Optional[int]:
        """Returns the maximum length of the stack."""
        return self._maxlen

    @property
    def top(self) -> Any:
        """Returns the top element of the stack.

        Raises
        ------
        IndexError
            if empty.
        """
        return self._stack[-1]


MSGS = ["ok", "error", "bye"]


if __name__ == "__main__":
    stack = Stack()
    while True:
        cmd = input().split()
        match cmd[0]:
            case "push":
                stack.push(cmd[1])
                msg = MSGS[0]
            case "pop":
                if not stack.is_empty():
                    msg = stack.pop()
                else:
                    msg = MSGS[1]
            case "back":
                if not stack.is_empty():
                    msg = str(stack.top)
                else:
                    msg = MSGS[1]
            case "size":
                msg = str(len(stack))
            case "clear":
                stack.clear()
                msg = MSGS[0]
            case "exit":
                print(MSGS[2])
                break
            case _:
                msg = MSGS[1]
        print(msg)
