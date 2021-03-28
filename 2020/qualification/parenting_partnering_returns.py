import sys

def solve():
    n = int(input())
    sch = []
    for i in range(n):
        sch.append(list(map(int, input().split())))
    sor = sorted(sch, key=lambda x: x[0])

    t1 = [False]*(60*24)
    t2 = [False]*(60*24)
    res = ['x']*n

    for s in sor:
        if True in t1[s[0]:s[1]]:
            if True in t2[s[0]:s[1]]:
                return "IMPOSSIBLE"
            else:
                t2[s[0]:s[1]] = [True]*(s[1]-s[0])
                res[sch.index(s)] = 'J'
                sch[sch.index(s)] = []
        else:
            t1[s[0]:s[1]] = [True]*(s[1]-s[0])
            res[sch.index(s)] = 'C'
            sch[sch.index(s)] = []
        #print(str(t1) + " " + str(t2))

    return "".join(res)

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))