import numpy as np
directs = "LURD"
def visualize(map, rope):
    cp = map.copy().astype(str)
    for i, r in enumerate(rope):
        cp[r[0]][r[1]] = i if i != 0 else 'H'
    print(cp)

with open('day9In.txt') as f:
    lines = f.readlines()

    vis = np.zeros((4, 4)).astype(int)
    r = [[0, 0] for _ in range(10)]
    rot = lambda x, y, n: [n-1-y, x]

    for line in lines:
        di = line[0]
        for _ in range(directs.index(di)):
            for i in range(len(r)):
                r[i] = rot(r[i][0], r[i][1], vis.shape[1])
            vis = np.rot90(vis)
        for _ in range(int(line.strip().split(" ")[1])):
            if r[0][1] == 0:
                vis = np.insert(vis, 0, np.zeros((vis.shape[0])), axis=1)
                for i in range(1,len(r)):
                    r[i][1] += 1
            else:
                r[0][1] -= 1
            for i in range(1,len(r)):
                xDiff = r[i-1][0] - r[i][0]
                yDiff = r[i-1][1] - r[i][1]
                if abs(yDiff) >= 2 and abs(xDiff) >= 2:
                    r[i][0] = r[i-1][0] - (xDiff//abs(xDiff))
                    r[i][1] = r[i-1][1] - (yDiff//abs(yDiff)) 
                elif abs(yDiff) >= 2 :
                    r[i][1] = r[i-1][1] - (yDiff//abs(yDiff)) 
                    r[i][0] = r[i-1][0]
                elif abs(xDiff) >= 2:
                    r[i][1] = r[i-1][1]
                    r[i][0] = r[i-1][0] - (xDiff//abs(xDiff))
            vis[r[-1][0]][r[-1][1]] |= 1
        for _ in range(4 - directs.index(di)):
            for i in range(len(r)):
                r[i] = rot(r[i][0], r[i][1], vis.shape[1])
            vis = np.rot90(vis)
        
    print(np.sum(vis))