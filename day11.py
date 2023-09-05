import numpy as np
from math import gcd
import time

def lcm(intLi):
    res = 1
    for x in intLi:
        res = res * x // gcd(res, x) 
    return res


with open('day11In.txt') as f:
    lines = f.readlines()
    monkeIte = []
    monkeLamb = []
    test = []
    throwT = []
    throwF = []
    monkeInsp = []

    mId = -1
    for line in lines:
        if 'Monkey' in line:
            mId += 1
            monkeInsp.append(0)
        elif 'Starting' in line:
            monkeIte.append([int(x) for x in line.split(": ")[1].split(",")])
        elif 'Operation' in line:
            funcStr =  line.split("= ")[1]
            monkeLamb.append(funcStr)
        elif 'Test' in line:
            test.append(int(line.split("by ")[1]))
        elif 'true:' in line:
            throwT.append(int(line.split("monkey ")[1]))
        elif 'false:' in line:
            throwF.append(int(line.split("monkey ")[1]))

    divBy = np.prod(test)

    man = False

    for round in range(10000):
        for i in range(len(monkeIte)):
            num = len(monkeIte[i])
            currentItems = monkeIte[i].copy()
            monkeIte[i] = []
            monkeInsp[i] += num
            for item in currentItems:
                mFunc = lambda x: eval(monkeLamb[i].strip())
                func = monkeLamb[i].strip()
                newVal = int(item)
                if "old * old" in func:
                    newVal  *= int(newVal)
                elif "*" in func:
                    newVal *= int(func[-2:])
                elif "+" in func:
                    newVal += int(func[-1:])
                else:
                    print("ERROR")
                    exit()

                # Part 1 
                # newVal = newVal // 3
                # Part 2

                newVal = newVal % divBy 
                # if newVal < 0:
                #     newFunc = lambda x: int(x) * int(x)
                #     print(newVal, item, monkeLamb[i])
                #     print((58558 * 58558))
                #     print(mFunc(58558))
                #     print(mFunc(item))
                #     print(newFunc(item))
                # newVal = newVal % divBy

                testCheck = newVal % test[i] == 0

                if testCheck:
                    monkeIte[throwT[i]].append(newVal)
                else:
                    monkeIte[throwF[i]].append(newVal)
    
    print(monkeInsp)
    monkeInsp.sort()
    out = np.prod(monkeInsp[-2:],dtype='int64')
    print(out)
