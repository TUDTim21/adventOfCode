import numpy as np

with open('test.txt') as f:
    lines = f.readlines()

    samples = [x for x in range(20, 221, 40)]

    print(samples)
    output = [] 
    val = 1
    total = 1
    outString = ""
    step = 1
    for line in lines:
        sH = total + 1
        for cycle in range( sH- step, sH ):
            cycle = (cycle )% 40  
            print(cycle)
            outString += "#" if cycle in [val -1 , val, val+1] else "."
            if cycle == 0:
                outString += "\n"
        cmd = line[:4]
        if cmd == 'noop' :
            step = 1
            total += 1
            if total in samples:
                output.append(total  * val)
        elif cmd == 'addx':
            step = 2
            addV = int(line.split(" ")[1])
            total+= 2
            if total - 1 in samples:
                output.append((total-1)  * val)
            val += addV
            if total in samples:
                output.append(total  * val)
        
    print(sum(output))
        
    print(outString)

