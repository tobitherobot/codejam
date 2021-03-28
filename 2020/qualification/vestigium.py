import sys

def solve():
    n = int(input())
    mtx = []
    
    for i in range(n):
        mtx.append([int(j) for j in input().split()])

    k = sum(mtx[i][i] for i in range(n))
    r = 0
    c = 0

    for i in range(n):
        if len(mtx[i]) != len(set(mtx[i])):
            r += 1
        if (len([row[i] for row in mtx]) != len(set([row[i] for row in mtx]))):
            c += 1

    return "{} {} {}".format(k, r, c)

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))