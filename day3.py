import numpy as np
from functools import reduce

with open('day3In.txt') as f:
    lines = f.readlines()

    # Part 1
    sum = 0
    for line in lines:
        one = line[:len(line)//2]
        two = line[len(line)//2:]
        both = set(one).intersection(set(two))
        val = both.pop()
        sum += (ord(val) - ord('A') + 26) % 52 + 1
        sum -= 6 if ord(val) >= 97 else 0
    print(sum)
        
    # Part 2
    sum = 0

    groups = np.array(lines)
    groups = np.split(groups, groups.size/3)

    for group in groups:
        group = [string.strip() for string in group]
        print(group)
        val = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
        sum += (ord(val) - ord('A') + 26) % 52 + 1
        sum -= 6 if ord(val) >= 97 else 0
    print(sum)