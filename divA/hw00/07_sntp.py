#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45469/problems/7/"""

# pylint: disable=invalid-name


from datetime import time, timedelta
from math import ceil


def _to_timedelta(atime: time) -> timedelta:
    """Casts time to timedelta object."""
    return timedelta(
        hours=atime.hour,
        minutes=atime.minute,
        seconds=atime.second,
    )


def _to_time(span: timedelta) -> time:
    """Returns time from timedelta total seconds."""
    seconds = ceil(span.total_seconds())
    days = seconds // 86400
    seconds -= days * 86400
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    return time(
        hour=hours,
        minute=minutes,
        second=seconds,
    )


if __name__ == "__main__":
    ta1 = _to_timedelta(time.fromisoformat(input()))
    tb1 = _to_timedelta(time.fromisoformat(input()))
    ta2 = _to_timedelta(time.fromisoformat(input()))
    tb2 = tb1 + timedelta(seconds=(ta2 - ta1).seconds) // 2
    print(_to_time(tb2))
