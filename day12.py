import numpy as np
from math import sqrt
def inBounds(m ,n, co):
    return co[0] >= 0 and co[0] < m and co[1] < n and co[1] >= 0 

def wasVisited(visArr, co):
    return visArr[co[0]][co[1]] == 1

def ordOfPos(hMap, co):
    return ord(hMap[co[0]][co[1]])

def distFunc(co1, co2):
    return abs(co1[0]-co2[0]) + abs(co1[1] - co2[1])

def otherDistFunc(co1, co2):
    return sqrt(abs(co1[0]-co2[0])**2 + abs(co1[1] - co2[1]))

with open('day12.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    m, n = len(lines), len(lines[0])

    hMap = np.array([[*line] for line in lines])
    end = np.where(hMap == 'E')
    start = np.where(hMap == 'S')


    endPos = list(zip(end[0], end[1]))[0]
    strPos = list(zip(start[0], start[1]))[0]
    hMap[endPos[0]][endPos[1]] = 'z'
    hMap[strPos[0]][strPos[1]] = 'a'
    # print(strPos)
    # print(ordOfPos(hMap, strPos))
    strPos = (strPos[0]-1, strPos[1] + 1)
    toCheck = [(strPos, 0)]
    visited = np.zeros((m, n))

    cnt = 0
    while (len(toCheck) >0) :
        curr = toCheck.pop()
        currPos = curr[0]
        if currPos ==  endPos:
            print(curr)
            break
        currMin = curr[1]
        hStr = hMap[currPos[0]][currPos[1]]
        currH = ord(hMap[currPos[0]][currPos[1]]) 
        visited[currPos[0]][currPos[1]] = 1 
        newPos = []
        for xo in range(-1, 2, 2):
            newPos.append((currPos[0] + xo, currPos[1] ))
        for yo in range(-1, 2, 2):
            newPos.append((currPos[0], currPos[1] + yo))
        newPos = list(filter(lambda pos: inBounds(m, n, pos), newPos))
        newPos = list(filter(lambda pos: not wasVisited(visited, pos), newPos))
        newPos = list(filter(lambda pos: ord(hMap[pos[0]][pos[1]]) <= currH + 1, newPos))
        newPos = sorted(newPos, key=lambda x: distFunc(endPos, x) )
        # newPos = sorted(newPos, key=lambda x: ordOfPos(hMap, x), reverse=True)
        newCheck = [(pos, currMin + 1) for pos in newPos]

        toCheck = newCheck + toCheck
        cnt += 1
        # break
        if cnt > 50000:
            print(toCheck[:5])
            break
