import sys
input = sys.stdin.readline

def go(arr, sm, s, y):
    if y > 3:
        return

    if sm == 7:
        if s >= 4:
            arr.sort()
            ans.add(tuple(arr))
        return

    temps = []
    for i in range(len(arr)):
        for x in range(4):
            nr = arr[i][0] + dirs[x][0]
            nc = arr[i][1] + dirs[x][1]
            if 0 <= nr < 5 and 0 <= nc < 5:
                if (nr,nc) not in arr and [nr,nc] not in temps:
                   temps.append([nr,nc])

    for i in range(len(temps)):
        r, c = temps[i][0], temps[i][1]
        if maps[r][c] == "S":
            go(arr+[(r,c)], sm+1, s+1, y)
        else:
            go(arr+[(r,c)], sm+1, s, y+1)

maps = [list(input()) for _ in range(5)]
dirs = [(0,1),(0,-1),(-1,0),(1,0)]
ans = set()
for i in range(5):
    for x in range(5):
        go([(i,x)], 1, 0, 0) # sum, s, y

print(len(ans))

# Pass