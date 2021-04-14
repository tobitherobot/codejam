# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c

def solve():
    l = int(input())
    array = list(map(int, input().strip().split(" ")))
    sum = 0

    # for every value of the array except the last one
    for i in range(l-1):
        # get index of smallest value starting from index i
        j = array.index(min(array[i:]))

        # create subarray and flip it
        sub = array[i:j+1]
        array = array[:i] + sub[::-1] + array[j+1:]

        # add the difference of both indexes
        sum += j-i+1

    return str(sum)

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))