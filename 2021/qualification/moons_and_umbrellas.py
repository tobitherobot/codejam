import sys

def solve():
    x, y, s = input().split()
    sum = 0
    c = s[0]

    for i in range(1, len(s)):
        if c=='C' and s[i]=='J':
            sum += int(x)
        elif c=='J' and s[i]=='C':
            sum += int(y)

        if s[i]!='?':
            c = s[i]

    return str(sum)

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))