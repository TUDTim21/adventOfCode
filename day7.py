
class Node:

    def __init__(self,name, t, size, p, c):
        self.name = name
        self.t = t
        self.size = size
        self.p = p
        self.c = c

    def findChild(self, chName):
        for ch in self.c:
            if ch.name == chName:
                return ch

def getTotalSizeDir(node):
    if node.t == 'f':
        return node.size
    fs  = 0
    ds = 0
    for cNode in node.c:

        if cNode.t == 'd':
            ds += getTotalSizeDir(cNode)
        else:
            fs += getTotalSizeDir(cNode)

    node.size = fs + ds 
    return fs + ds  

def getVals(node, ammount):
    if node.t == 'f':
        return 0
    value = 0;
    if node.size <= ammount:
        value += node.size
    for cNode in node.c:
        value += getVals(cNode, ammount)
    return value

def getDirSizeSet(node):
    if node.t == 'f':
        return set()
    arr = set([node.size])
    for cNode in node.c:
        arr.update(getDirSizeSet(cNode))
    return arr

with open('day7In.txt') as f:
    lines = f.readlines()

    struct = ['/']

    main = Node("/", 'd', 0, None, [])
    current = main

    for line in lines[1:]:
        line = line.strip()
        if line[0]  == '$':
            cmd = line[2:4]
            if cmd == "cd":
                if line[-2:] == "..":
                    current = current.p
                else:
                    dirN = line[5:]
                    current = current.findChild(dirN) 
            elif cmd == "ls":
                pass
        elif line[:3] == 'dir':
            current.c.append(Node(line[4:],'d', 0, current, []))
        else:
            current.c.append(Node(line.split(" ")[1], 'f', int(line.split(" ")[0]), current, None))
    print( getTotalSizeDir(main))

    # Part 1
    print(getVals(main, 100000))

    # Part 2
    toFree = main.size - (70000000 - 30000000)
    print(toFree)
    values =  list(getDirSizeSet(main))
    values.sort()
    for value in values:
        if value >= toFree:
            print(value)
            break

            