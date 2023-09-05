import numpy as np

with open('day2In.txt') as f:
    lines =f.readlines()

    # Part 1
    dictVal = {"A": "ZXY", 
    "B": "XYZ", 
    "C": "YZX" }
    sum =0
    for line in lines:
        sum += dictVal[line[0]].find(line[2]) * 3
        sum += dictVal["B"].find(line[2]) + 1

    print(sum)
    # Part 2

    # ABC 123
    dictValP2 = {"X": "BCA",
    "Y": "ABC",
    "Z": "CAB" }
    sum =0
    for line in lines:
        sum += dictValP2[line[2]].find(line[0]) + 1
        sum += dictVal["B"].find(line[2]) * 3
     
    print(sum)