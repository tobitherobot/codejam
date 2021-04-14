# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

def solve():
    x, y, s = input().strip().split(" ")
    cj, jc = int(x), int(y)
    
    # two variables to compare both possibilities
    # set both to infinity for max value
    INF = int(1e10)
    last_c, last_j = INF, INF

    # depending on how the string starts the variables are set to zero
    if s[0]!='C':
        last_j = 0
    if s[0]!='J':
        last_c = 0

    for i in range(1, len(s)):
        if s[i]=='C':
            # set last_c to the least possible value
            # reset last_j to ininity
            last_c = min(last_c, last_j + jc)
            last_j = INF
        elif s[i]=='J':
            # set last_j to the least possible value
            # reset last_c to infinity
            last_j = min(last_j, last_c + cj)
            last_c = INF
        else: # ?
            # set both values to the smallest possible value
            last_c, last_j = min(last_c, last_j + jc), min(last_j, last_c + cj)

    return str(min(last_c, last_j))

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))