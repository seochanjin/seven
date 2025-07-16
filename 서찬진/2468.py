import sys
sys.setrecursionlimit(10**6)
 
input = sys.stdin.readline
n = int(input())

a=[]
for i in range(n):
    a.append(list(map(int, input().split())))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]


def dfs(x,y,h,visited):
    visited[x][y] = True
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and a[nx][ny] > h:
                dfs(nx, ny, h, visited)

max_safe = 0

for h in range(0, 101):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and a[i][j] > h:
                dfs(i, j, h, visited)
                count += 1
    max_safe = max(max_safe, count)

print(max_safe)

