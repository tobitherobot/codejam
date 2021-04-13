# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5

def solve():
    n = int(input())
    x = list(map(int, input().strip().split(" ")))
    
    c = 0
    a = x[0]

    # compare every value with the previous value
    # update the previous value to smallest possible value
    for b in x[1:]:
        if a < b:
            a = b
            continue
        m = 1
        while True:
            m *= 10
            c += 1

            # if previous value is smaller by appending m 9s
            if a < (b+1)*m-1:
                if a < b*m:
                    # if previous value is still smaller by only appending 0s with multiplier m
                    # then smallest possible next value is b*m
                    a = b*m
                else:
                    # if not, the next smallest possible value is one bigger than b*m plus the previous overflow  
                    # example: 99 99 99
                    a = b*m + (a%m) + 1
                break    

    return c

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))