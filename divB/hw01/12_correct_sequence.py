#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/12/"""

# pylint: disable=invalid-name


from typing import List, Sequence


def is_correct_delimeters(
    lefty: Sequence,
    righty: Sequence,
) -> bool:
    """Evaluates sequences to be correct left-right delimeter sequences.

    Two sequences are correct left-right delimeters if:
        * their lengths are equal;
        * they have no common elements.

    Parameters
    ----------
    lefty : Sequence
        delimeters from the left
    righty : Sequence
        delimeters from the right

    Raises
    ------
    bool
    """
    if len(lefty) != len(righty):
        return False
    if set(lefty) & set(righty):
        return False
    return True


def is_correct_sequence(
    seq: Sequence,
    lefty: Sequence,
    righty: Sequence,
) -> bool:
    """Matches the sequence of delimiters to form a correct sequence.

    Parameters
    ----------
    seq: Sequence,
    lefty: Sequence
    righty: Sequence

    Raises
    ------
    ValueError
        If delimeters are not correct sequences.
        See `is_correct_delimeters` function.

    Returns
    -------
    bool
    """
    if not is_correct_delimeters(lefty, righty):
        raise ValueError("bad delimeters")
    stack: List[str] = []
    for item in seq:
        if item in lefty:
            stack.append(item)
        if item in righty:
            if not stack:
                return False
            if lefty.index(stack.pop()) != righty.index(item):
                return False
    return not stack  # if is empty


if __name__ == "__main__":
    sequence = input()
    print(
        "yes"
        if is_correct_sequence(
            sequence, lefty="([{", righty=")]}"
        )
        else "no"
    )
