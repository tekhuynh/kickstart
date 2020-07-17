def func():
    n, d = [int(i) for i in input().split()]
    x = reversed([int(i) for i in input().split()])

    for xi in x:
        d -= d % xi
    
    return d


t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))