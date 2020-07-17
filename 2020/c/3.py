def func():
    n = int(input())
    a = [int(x) for x in input().split()]

    sums = [0]
    maxa = -100
    for i in range(n):
        if a[i] > maxa:
            maxa = a[i]
        sums.append(sums[-1] + a[i])
    
    squares = set([x**2 for x in range(maxa * n)])

    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            print(i, j, sums[j] - sums[i])
            if sums[j] - sums[i] in squares:
                count += 1

    return sums

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))