import numpy as np

with open('day1InputData.txt') as f:
    # part 1
    lines = f.readlines()
    values = [0] * 2270;
    ind = 0
    for line in lines:
        if line.strip() == "":
            ind += 1
            continue
        else:
            values[ind]+= int(line.strip())
    sol = np.max(values)
    print(sol)

    # part 2

    values = np.sort(values)

    sol = np.sum(values[-3:])
    print(sol)