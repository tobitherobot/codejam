# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

def solve():
    s = input()
    sn = ""
    curr = 0

    for c in s:
        n = int(c)
        if curr < n:
            # if the current brackets are less than the current digit, add opening brackets and add the difference
            sn += '('*(n-curr)
            curr += (n-curr)
        else:
            # if the current brackets are more than the current digit, add closing brackets and remove the difference
            sn += ')'*(curr-n)
            curr -= (curr-n)
        # add the digit itself
        sn += str(n)

    # as the last step, add closing brackets if necessary
    sn += ')'*curr
    return sn

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))