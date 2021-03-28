import sys

def solve():
    n, c = map(int, input().split())
    sum = 0
    
    if c < n-1 or (n*n+n)/2-1 < c:
        return "IMPOSSIBLE"

    seq = get_seq(n, c)
    array = [0]*n
    flip = 0
    n = 1

    for b in seq:
        if b:
            array = array[::-1]
            flip += 1
        for i in range(0, n):
            if array[i]==0:
                array[i] = n
                n += 1
                break

    array[array.index(min(array))] = n

    if flip%2==1:
        array = array[::-1]

    return " ".join(list(map(str, array)))

def get_seq(n, c):
    seq = [False]*(n-1)
    c -= (n-1)

    for i in range(n-1, 0, -1):
        if i <= c:
            seq[n-1-i] = True
            c -= i
    
    return seq

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))