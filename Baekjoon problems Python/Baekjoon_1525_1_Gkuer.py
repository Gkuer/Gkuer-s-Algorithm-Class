import sys
from collections import deque
input = sys.stdin.readline
dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs():
    q = deque()
    q.append(first)
    maps[first] = 0
    while q:
        data = q.popleft()

        if data == "123456789":
            return True

        temp = data
        pos = data.index("9")
        idx = pos // 3
        idy = pos % 3

        for i in range(4):
            nr = idx + dirs[i][0]
            nc = idy + dirs[i][1]
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_pos = nr * 3 + nc
                new_data = list(data)
                new_data[pos], new_data[new_pos] = new_data[new_pos], new_data[pos]
                new_data = ''.join(new_data)
                if new_data not in maps:
                    maps[new_data] = maps[temp] + 1
                    q.append(new_data)

    return False

first = ""
for i in range(3):
    temp = "".join(input().split())
    first += temp

first = first.replace("0","9")

maps = {}
res = bfs()

print(maps['123456789'] if res else -1)

# Pass