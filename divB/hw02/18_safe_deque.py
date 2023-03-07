#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/18/"""

# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=duplicate-code


from collections import deque


MSGS = ["ok", "error", "bye"]


if __name__ == "__main__":
    dequeue: deque = deque()
    while True:
        cmd = input().split()
        match cmd[0]:
            case "push_front":
                dequeue.appendleft(cmd[1])
                msg = MSGS[0]
            case "push_back":
                dequeue.append(cmd[1])
                msg = MSGS[0]
            case "pop_front":
                if dequeue:
                    msg = dequeue.popleft()
                else:
                    msg = MSGS[1]
            case "pop_back":
                if dequeue:
                    msg = dequeue.pop()
                else:
                    msg = MSGS[1]
            case "front":
                if dequeue:
                    msg = str(dequeue[0])
                else:
                    msg = MSGS[1]
            case "back":
                if dequeue:
                    msg = str(dequeue[-1])
                else:
                    msg = MSGS[1]
            case "size":
                msg = str(len(dequeue))
            case "clear":
                dequeue.clear()
                msg = MSGS[0]
            case "exit":
                print(MSGS[2])
                break
            case _:
                msg = MSGS[1]
        print(msg)
