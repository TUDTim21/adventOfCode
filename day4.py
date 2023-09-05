import numpy as np
from functools import reduce

with open('day4In.txt') as f:
    lines = f.readlines()

    # Part 1
    sum = 0
    for line in lines:
        left, right = line.split(",")[:2]
        ll, lh = [int(num) for num in left.split("-")]
        rl, rh = [int(num) for num in right.split("-")]
        if ((ll <= rl and lh >= rh) or (ll >= rl and lh <= rh)):
            sum += 1
    print(sum)

    # Part 2
    sum = 0
    for line in lines:
        left, right = line.split(",")[:2]
        ll, lh = [int(num) for num in left.split("-")]
        rl, rh = [int(num) for num in right.split("-")]
        if ((rl <= lh and lh <= rh) or (rl <= ll and ll <= rh)):
            sum += 1
        elif ((ll <= rh and rh <= lh) or (ll <= rl and rl <= lh)):
            sum += 1
        elif ((ll <= rl and lh >= rh) or (ll >= rl and lh <= rh)):
            sum += 1

    print(sum)
