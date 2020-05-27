def func():
    n, k, p = map(int, input().split())
    plates = []
    for i in range(n):
        plates.append(list(map(int, input().split())))
    memo = dict()
    maxsum = max_beauty(plates, 0, p, memo)
    print(memo)
    return maxsum

def max_beauty(plates, stack, p, memo):
    if stack >= len(plates):
        return 0
    
    if key(stack, p) in memo:
        return memo[key(stack, p)]

    maxscore = max_beauty(plates, stack + 1, p, memo)

    stacksum = 0
    plates_remaining = p
    for plate in plates[stack]:
        if plates_remaining == 0:
            break
        stacksum += plate
        plates_remaining -= 1
        nextstack = max_beauty(plates, stack + 1, plates_remaining, memo)
        maxscore = max(maxscore, stacksum + nextstack)

    memo[key(stack, p)] = maxscore
    return maxscore

def key(stack, p):
    return "{}-{}".format(stack, p)


t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, func()))