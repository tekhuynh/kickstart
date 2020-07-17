def func():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    counting = False
    count = 0
    prev = 0
    for x in a[::-1]:
        if x == 1:
            counting = True
            prev = 1
        elif counting == True and x - prev != 1:
            counting = False
        elif counting == True and x - prev == 1:
            prev = x
        
        if counting == True and prev == k:
            count += 1

    return count





t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))