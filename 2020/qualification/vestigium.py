# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

def solve():
    n = int(input())
    mtx = []
    
    for i in range(n):
        mtx.append(list(map(int, input().split())))

    r = 0
    c = 0

    # get sum of diagonal
    k = sum(mtx[i][i] for i in range(n))

    for i in range(n):
        # check for repeating values in each row
        if len(mtx[i]) != len(set(mtx[i])):
            r += 1
        # check for repeating values in each column
        if (len([row[i] for row in mtx]) != len(set([row[i] for row in mtx]))):
            c += 1

    return "{} {} {}".format(k, r, c)

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))