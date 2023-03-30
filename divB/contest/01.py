#!/usr/bin/env python3


from collections import defaultdict


goods = defaultdict(int)

ops = int(input())

cars = []
for _ in range(ops):
    cmd, *opts = input().split()
    match cmd:
        case "add":
            cars.append((opts[1], int(opts[0])))
            goods[opts[1]] += int(opts[0])
        case "delete":
            total = int(opts[0])
            while cars and total > 0:
                good, amount = cars[-1]
                amount = min(amount, total)
                goods[good] -= amount
                total -= amount
                diff = cars[-1][1] - amount
                if total or diff == 0:
                    cars.pop()
                else:
                    cars[-1] = (good, diff)
        case "get":
            print(goods[opts[0]])
        case _:
            raise RuntimeError()
