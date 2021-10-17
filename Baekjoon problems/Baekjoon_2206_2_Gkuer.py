import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_idx,start_idy):
    q = deque()
    q.append([start_idx, start_idy,1])
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        r, c, flag = q.popleft()
        if r == n-1 and c == m-1:
            return visited[r][c][flag]
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 1 and flag == 1:
                    visited[nr][nc][0] = visited[r][c][1] + 1
                    q.append([nr,nc,0])
                elif maps[nr][nc] == 0 and visited[nr][nc][flag] == 0:
                    visited[nr][nc][flag] = visited[r][c][flag] + 1
                    q.append([nr,nc,flag])
    return -1

n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

print(bfs(0, 0))

# Pass