def func():
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in a:
        if b < i:
            break
        b -= i
        count += 1

    return count

t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))