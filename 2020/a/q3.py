import math

def case():
    n, k = [int(x) for x in input().split()]
    sessions = [int(x) for x in input().split()]

    d = find(sessions, 1, 10**9, k)
    return d

def find(sessions, dmin, dmax, ktarget):
    if dmax - dmin == 1:
        kdmin = findk(sessions, dmin)
        if kdmin <= ktarget:
            return dmin
        return dmax

    mid = int((dmin + dmax)/2)
    k = findk(sessions, mid)
    if k > ktarget:
        return find(sessions, mid, dmax, ktarget)
    return find(sessions, dmin, mid, ktarget)
    
def findk(sessions, d):
    k = 0
    for i in range(1, len(sessions)):
        k += math.ceil((sessions[i]-sessions[i-1])/d) - 1
    return k


t = int(input())
for i in range(1, t+1):
    print("Case #{}: {}".format(i, case()))