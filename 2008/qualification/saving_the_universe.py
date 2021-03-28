import sys

def solve():
    e = []
    s = int(input())
    for i in range(s):
        e.append(input())
    
    q = int(input())
    x = []
    sum = 0
    for i in range(q):
        m = input()
        x.append(m)
        if len(set(x))==s:
             x.clear()
             sum += 1
             x.append(m)
        
    return sum

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))