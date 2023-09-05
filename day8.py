# import sys
import numpy as np

# np.set_printoptions(threshold=9999)


with open('day8In.txt') as f:
    lines = f.readlines()
    m = len(lines)
    n = len(lines[0].strip())
    dp = np.zeros((m, n)).astype(int)
    h = np.array([[*line.strip()] for line in lines])
    for d in range(4):
        h = np.rot90(h)
        dp = np.rot90(dp)
        for i in range(h.shape[0]):
            mV = -1
            for j in range(h.shape[1]):
                if int(h[i][j]) > mV:
                    mV = int(h[i][j])
                    dp[i][j] |= 1
                
    print(np.sum(dp))

    # Part 2

    print(m, n)
    dp = np.ones((m, n)).astype(int)
    h = np.array([[*line.strip()] for line in lines])

    for i in range(1, m-1):
        for j in range(1, n- 1):
            o = 1
            curr = h[i][j]
            # Left
            while ((i-o) > 0 and h[i-o][j] < curr):
                o += 1
            dp[i][j] *= o

            # Right
            o = 1
            while ((i + o) < m - 1 and h[i+o][j] < curr):
                o += 1
            dp[i][j] *= o

            # Up
            o = 1
            while ((j - o) > 0  and h[i][j - o] < curr):
                o += 1
            dp[i][j] *= o

            # Down
            o = 1
            while ((j + o) < n - 1 and h[i][j + o] < curr):
                o += 1
            dp[i][j] *= o
    
    print(np.max(dp))



    # for d in range(4):
    #     for i in range(h.shape[0]):
    #         mV = -1
    #         for j in range(1, h.shape[1]):
    #             if int(h[i][j]) > mV:
    #                 aDp[d][i][j] = aDp[d][i][j-1]+ 1 
    #                 prev = aDp[d][i][j]
    #                 while (j - prev > 0 and int(h[i][j-prev]) < int(h[i][j])):
    #                     aDp[d][i][j] += aDp[d][i][j-prev] 
    #                     prev = aDp[d][i][j]
    #             else:
    #                 aDp[d][i][j] = 1
    #             mV = int(h[i][j])
    #     h = np.rot90(h)

    # for i in range(3):
    #     for j in range(i+1,4):
    #         aDp[j] = np.rot90(aDp[j])

    # finalDp = np.ones((m, n))
        
    # for arr in aDp:
    #     finalDp = np.multiply(finalDp, arr)
    #     print(finalDp.astype(int))

    # print(int(np.max(finalDp).astype(int)))