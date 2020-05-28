def cases():
    n, k, p = map(int, input().split())
    stacks = []
    for i in range(n):
        stacks.append([int(x) for x in input().split()])
    memo = dict()
    maxsum = plates(stacks, 0, p, memo)
    return maxsum

def plates(stacks, stack_num, plates_remaining, memo):
    if stack_num == len(stacks):
        return 0
    
    currkey = key(stack_num, plates_remaining)
    if currkey in memo:
        return memo[currkey]

    maxsum = plates(stacks, stack_num + 1, plates_remaining, memo)

    cumsum = 0
    for plate in stacks[stack_num]:
        if plates_remaining == 0:
            break
        cumsum += plate
        plates_remaining -= 1
        next_stack = cumsum + plates(stacks, stack_num + 1, plates_remaining, memo)
        maxsum = max(maxsum, next_stack)
    
    memo[currkey] = maxsum
    return maxsum

def key(k1, k2):
    return "{}-{}".format(k1, k2)


t = int(input())
for i in range(t):
    print("Case #{}: {}".format(i + 1, cases()))