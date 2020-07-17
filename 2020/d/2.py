def func():
    k = int(input())
    a = [int(x) for x in input().split()]

    count = 0
    up = 0
    down = 0
    for i in range(1, k):
        if a[i-1] < a[i]:
            up += 1
            down = 0
        elif a[i-1] > a[i]:
            down += 1
            up = 0
        if up > 3 or down > 3:
            count += 1
            up = 0
            down = 0
        
    return count


t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))