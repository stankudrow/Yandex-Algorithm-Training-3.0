#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/16/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


from typing import Any, Optional, Sequence


class QueueError(Exception):
    """Generic Queue Exception."""


class Queue:
    """The Queue data structure."""

    def __init__(
        self,
        seq: Optional[Sequence] = None,
        maxlen: Optional[int] = None,
    ):
        self._queue = [] if seq is None else list(seq)
        if maxlen and maxlen < 0:
            raise QueueError(f"maxlen (={maxlen}) < 0")
        self._maxlen = maxlen
        self._head = 0

    def __bool__(self) -> bool:
        return bool(len(self))

    def __len__(self) -> int:
        return (
            len(self._queue[self._head :]) if self._queue else 0
        )

    def __repr__(self) -> str:
        return f"Queue({self._queue})"

    def _squeeze(self):
        """Reduces the size of the queue after excedding the half of the queue."""
        if self._head > len(self) // 2:
            self._queue = self._queue[self._head :]
            self._head = 0

    def clear(self):
        """Clears the queue, making it empty."""
        self._queue.clear()
        self._head = 0

    def is_empty(self) -> bool:
        """Returns True if the queue is empty."""
        return not bool(self)

    def extend(self, seq: Sequence):
        """Pushes the elements from the sequence."""
        self._squeeze()
        lst = list(seq)
        if self.maxlen is None:
            cap = len(lst)
        else:
            cap = min(len(lst), self.maxlen - len(self))
        for idx in range(cap):
            self._queue.append(lst[idx])

    def dequeue(self) -> Any:
        """Pops the first/front element.

        Raises
        ------
        IndexError
            if empty.
        """
        item = self._queue[self._head]
        self._head += 1
        self._squeeze()
        return item

    def enqueue(self, value: Any):
        """Pushes the value into the queue."""
        if self.maxlen is None or (
            (self.maxlen is not None) and len(self) < self.maxlen
        ):
            self._queue.append(value)
        else:
            raise QueueError(
                f"cannot exceed maxlen ({self.maxlen})"
            )

    @property
    def front(self) -> Any:
        """Returns the first/front element of the queue.

        Raises
        ------
        IndexError
            if empty.
        """
        return self._queue[self._head]

    @property
    def maxlen(self) -> Optional[int]:
        """Returns the maximum length of the stack."""
        return self._maxlen


MSGS = ["ok", "error", "bye"]


if __name__ == "__main__":
    queue = Queue()
    while True:
        cmd = input().split()
        match cmd[0]:
            case "push":
                queue.enqueue(cmd[1])
                msg = MSGS[0]
            case "pop":
                if not queue.is_empty():
                    msg = queue.dequeue()
                else:
                    msg = MSGS[1]
            case "front":
                if not queue.is_empty():
                    msg = str(queue.front)
                else:
                    msg = MSGS[1]
            case "size":
                msg = str(len(queue))
            case "clear":
                queue.clear()
                msg = MSGS[0]
            case "exit":
                print(MSGS[2])
                break
            case _:
                msg = MSGS[1]
        print(msg)
