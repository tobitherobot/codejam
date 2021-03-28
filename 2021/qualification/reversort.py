import sys

def solve():
    l = int(input())
    sum = 0
    array = [int(j) for j in input().split(" ")]

    for i in range(l-1):
        j = array.index(min(array[i:]))
        sub = array[i:j+1]
        array = array[:i] + sub[::-1] + array[j+1:]
        sum += j-i+1

    return str(sum)

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))