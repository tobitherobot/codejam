import sys

def solve():
    n = int(input())
    s = ""
    e = ""
    for i in range(n):
        x = input()
        while "**" in x:
            x = x.replace("**", "*")
        x = x.split("*")

        if 0<len(x[-1]):
            if e in x[-1]:
                e = x[-1]
            elif x[-1] in e:
                continue
            else:
                return "*"
            
    return e

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))