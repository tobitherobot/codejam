import sys

def solve():
    s = input()
    sn = ""
    curr = 0

    for c in s:
        n = int(c)
        while curr != n:
            if curr < n:
                sn += '('
                curr += 1
            else:
                sn += ')'
                curr -= 1
        sn += str(n)

    sn += ')'*curr
    return sn

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))