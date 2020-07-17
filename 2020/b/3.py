def func():
    s = input()

    w = 0
    h = 0
    mults = []
    mult = 1

    for c in s:
        if c.isdigit():
            mults.append(int(c))
            mult *= int(c)
        elif c == ")":
            mult //= mults.pop()
        elif c == "N":
            h -= mult
        elif c == "S":
            h += mult
        elif c == "E":
            w += mult
        elif c == "W":
            w -= mult

    w = w % 10 ** 9 + 1
    h = h % 10 ** 9 + 1

    return "{} {}".format(w, h)



t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))