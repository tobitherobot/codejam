# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

def solve():
    n = int(input())
    sch = []
    for i in range(n):
        sch.append(list(map(int, input().split())))

    # schedule sorted by start time
    sor = sorted(sch, key=lambda x: x[0])       

    # two timetables with max possible length, emtpy sections are False
    t1 = [False]*(60*24)
    t2 = [False]*(60*24)
    res = ['x']*n

    for s in sor:
        if True in t1[s[0]:s[1]]:
            if True in t2[s[0]:s[1]]:
                # if both timetables contain True in the section of the schedule, it's impossible
                return "IMPOSSIBLE"
            else:
                t2[s[0]:s[1]] = [True]*(s[1]-s[0])  # set section of the schedule in timetable 2 to True
                res[sch.index(s)] = 'J'             # set index in result to J (different order because sorted)
                sch[sch.index(s)] = []              # remove schedule (because of indexes of identical entries)
        else:
            t1[s[0]:s[1]] = [True]*(s[1]-s[0])
            res[sch.index(s)] = 'C'
            sch[sch.index(s)] = []

    return "".join(res)

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))