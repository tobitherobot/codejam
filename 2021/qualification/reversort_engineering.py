# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7

def solve():
    n, c = map(int, input().split())
    sum = 0
    
    # smallest possible cost: n-1
    # example: 1 2 3 4 5
    # biggest possible cost: (n*n+n)/2-1
    # example: 2 4 5 3 1
    if c < n-1 or (n*n+n)/2-1 < c:
        return "IMPOSSIBLE"

    seq = [False]*(n-1)
    c -= (n-1)
    flip = 0

    # if the costs allow it, place next digit at highest index for maximum cost 
    # mark that index as True for later
    for i in range(n-1, 0, -1):
        if i <= c:
            seq[n-1-i] = True
            flip += 1
            c -= i
    
    array = [0]*n
    n = 1

    # place numbers according to sequence
    # False: place number on next possible index
    # True: flip array, then place number on the next possible index
    for b in seq:
        if b:
            array = array[::-1]
        j = array.index(0)
        array[j] = n
        n += 1
    array[array.index(min(array))] = n

    # if flips are uneven, reverse the array to its initial position
    if flip%2==1:
        array = array[::-1]

    return " ".join(list(map(str, array)))

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))