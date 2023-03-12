#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/45468/problems/29/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


def make_purchases(
    days: int,
) -> None | list[tuple[int, list[int]]]:
    """Returns the states of purchases.

    If cost > 100, then a coupon is acquired,
    but only if the current purchase is done.
    Otherwise one can either use a coupon and save money,
    or pay and save a coupon for future purposes.
    """

    if days < 1:
        return None
    states: list[tuple[int, int]] = [(0, 0)]
    memo: list[tuple[int, list[int]]] = [(0, [0, 0, 0])]
    for nday in range(1, days + 1):
        cost = int(input())
        memo.append((cost, [0 for _ in range(3 + nday)]))
        coupon = 1 if cost > 100 else 0
        new_states: list[tuple[int, int]] = []
        for day, coupons in states:
            current_cost = memo[day][-1][coupons]
            if coupons:
                if memo[day + 1][-1][coupons + coupon]:
                    memo[day + 1][-1][coupons + coupon] = min(
                        current_cost + cost,
                        memo[day + 1][-1][coupons + coupon],
                    )
                else:
                    memo[day + 1][-1][coupons + coupon] = (
                        current_cost + cost
                    )
                new_states.append((day + 1, coupons + coupon))
                memo[day + 1][-1][coupons - 1] = current_cost
                new_states.append((day + 1, coupons - 1))
            else:
                if memo[day + 1][-1][coupons + coupon]:
                    memo[day + 1][-1][coupons + coupon] = min(
                        current_cost + cost,
                        memo[day + 1][-1][coupons + coupon],
                    )
                else:
                    memo[day + 1][-1][coupons + coupon] = (
                        current_cost + cost
                    )
                new_states.append((day + 1, coupons + coupon))
        states = sorted(set(new_states), reverse=True)
    return memo


if __name__ == "__main__":
    days = int(input())
    dynamics = make_purchases(days)
    if dynamics:
        coupons_left = 0
        costs = dynamics[-1][1]
        while (coupons_left < days + 3) and (
            costs[coupons_left] == 0
        ):
            coupons_left += 1
        while (coupons_left < days + 3) and (
            costs[coupons_left] == costs[coupons_left + 1]
        ):
            coupons_left += 1
        coupons_left = (
            0 if coupons_left == days + 3 else coupons_left
        )
        total_cost = costs[coupons_left]
        coupons = str(coupons_left)
        print(total_cost)
        coupon_days: list[int] = []
        for day in range(len(dynamics) - 1, 1, -1):
            prev_costs = dynamics[day - 1][1]
            curr_price = dynamics[day][0]
            if (
                total_cost
                == curr_price + prev_costs[coupons_left]
            ):
                total_cost = prev_costs[coupons_left]
            elif total_cost == prev_costs[coupons_left + 1]:
                coupons_left += 1
                coupon_days.append(day)
            else:
                coupons_left -= 1
                total_cost = prev_costs[coupons_left]
        print(f"{coupons} {len(coupon_days)}")
        print(*coupon_days[::-1], sep="\n")
    else:
        print("0\n0 0\n")
