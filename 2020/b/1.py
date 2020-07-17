def func():
    n = int(input())
    h = [int(x) for x in input().split()]

    peaks = 0
    for i in range(1, n - 1):
        if h[i] > h[i-1] and h[i] > h[i+1]:
            peaks += 1

    return peaks

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))