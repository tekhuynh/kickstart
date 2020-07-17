def func():
    n = int(input())
    v = [int(x) for x in input().split()]

    days = 0
    cmax = 0
    for i in range(n):
        larger_than_prev = i == 0 or v[i] > cmax
        larger_than_next = i == n - 1 or v[i] > v[i+1]
        if larger_than_prev and larger_than_next:
            days += 1
        cmax = max(cmax, v[i])
    
    return days

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))