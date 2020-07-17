def func():
    r, c = [int(x) for x in input().split()]
    wall = []
    for i in range(r):
        wall.append(input())


    letters = set()
    vertices = set()
    for i in range(c):
        cletter = None
        for j in range(r):
            letters.add(wall[j][i])
            if cletter == None:
                cletter = wall[j][i]
                continue
            if cletter != wall[j][i]:
                vertices.add((cletter, wall[j][i]))
                cletter = wall[j][i]

    order = []
    while letters:
        dependant = set([x[0] for x in vertices])
        independant = letters.difference(dependant)
        if not independant:
            return -1
        order += independant
        [letters.remove(x) for x in independant]
        toremove = [x for x in vertices if x[1] in independant]
        [vertices.remove(x) for x in toremove]

    return "".join(order)

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))