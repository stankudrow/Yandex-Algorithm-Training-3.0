#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45469/problems/4/"""

# pylint: disable=invalid-name


if __name__ == "__main__":
    pupils = int(input())  # 2 <= N <= 1e9
    # versions of tasks
    vers = int(input())  # 2 <= K <= N
    # Petia's row and seat:
    prow = int(input()) - 1  # from 1 since N // 2 >= 1 -> from 0
    pseat = int(input()) - 1  # 1 if right, 2 if left -> 0, 1
    # Petia's global seat
    g_pseat = 2 * prow + 1 * pseat
    left, right = g_pseat - vers, g_pseat + vers
    vrow_r, vseat_r = divmod(right, 2)
    vrow_l, vseat_l = divmod(left, 2)
    if right < pupils and (
        (vrow_r - prow) <= abs(prow - vrow_l)
    ):
        print(vrow_r + 1, vseat_r + 1, sep=" ")
    elif left > -1:
        print(vrow_l + 1, vseat_l + 1, sep=" ")
    else:
        print(-1)
