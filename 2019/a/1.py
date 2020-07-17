def func():
    n, p = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]

    s.sort()
    sums = []
    for i in range(n):
        if i == 0:
            sums.append(s[i])
        else:
            sums.append(s[i] + sums[i - 1])

    minhours = None
    for i in range(n-p+1):
        hours = p * s[i + p - 1] - sums[i + p - 1]
        if i != 0:
            hours += sums[i-1]
        if not minhours:
            minhours = hours
        else:
            minhours = min(minhours, hours)
        if minhours == 0:
            break
        

    return minhours

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))