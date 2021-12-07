import sys
input = sys.stdin.readline

def cal(arr,gate_depth):
    arr = sorted(arr)
    time = [0]*300
    for i in arr:
        i += 1
        while time[i] >= 3:
            i += 1
        for x in range(i,i+gate_depth):
            time[x] += 1

    for i in range(299,-1,-1):
        if time[i]:
            return i+1

def solve(arr,gate_info):
    if not arr:
        return 0

    res = []
    for idx, idy in arr:
        res.append(abs(gate_info[0] - idx) + abs(gate_info[1] - idy))

    return cal(res, gate_info[2])

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    people, gate = [], []
    for i in range(n):
        for x in range(n):
            if maps[i][x] == 1:
                people.append([i,x])
            elif maps[i][x] > 1:
                gate.append([i,x,maps[i][x]])

    ans = 10000000
    for i in range(1 << len(people)):
        group1, group2 = [], []
        for x in range(len(people)):
            if i & (1<<x):
                group1.append(people[x])
            else:
                group2.append(people[x])
        ans = min(ans,max(solve(group1,gate[0]),solve(group2,gate[1])))

    print("#{} {}".format(tc,ans))

# Pass