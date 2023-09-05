import numpy as np
from functools import reduce

with open('day5In.txt') as f:
    lines = f.readlines()

    stacks = [[] for i in range(9)] 
    for line in lines:
        if line[1] == '1':
            break
        for i in range(9):
            if (4*i+ 1 >= len(line)):
                break
            if line[4*i + 1] == " ":
                continue

            stacks[i].insert(0, line[4*i + 1])

    p2stacks = [stk.copy() for stk in stacks]
    # Part 1
    for line in lines:
        if line[:4] == 'move':
            a, whT = line.split('move')[1].split('from')
            a = int(a.strip())
            whT = [int(s.strip()) - 1 for s in whT.split('to')]
            for i in range(a):
                stacks[whT[1]].append(stacks[whT[0]].pop())
    out = ""
    for i in range(len(stacks)):

        if (len(stacks[i]) == 0): 
            out += " "
        else: out += stacks[i].pop()
    print(out)
    # Part 2

    for line in lines:
        if line[:4] == 'move':
            a, whT = line.split('move')[1].split('from')
            a = int(a.strip())
            whT = [int(s.strip()) - 1 for s in whT.split('to')]
            ind = len(p2stacks[whT[1]])
            for i in range(a):
                if len(p2stacks[whT[0]]) != 0:
                    p2stacks[whT[1]].insert(ind, p2stacks[whT[0]].pop())
    out = ""
    for i in range(len(p2stacks)):

        if (len(p2stacks[i]) == 0): 
            out += " "
        else: out += p2stacks[i].pop()
    print(out)