import sys
from collections import deque

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

WALL = '#'
PERSON = 'J'
FIRE = 'F'
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]

row, col = map(int, input().strip().split())
boards = [input().strip() for _ in range(row)]

visited = [[-1 for _ in range(col)] for _ in range(row)]

fires = []
for r in range(row):
    for c in range(col):
        if boards[r][c] == FIRE:
            visited[r][c] = 0
            fires.append((r, c))


def findJ():
    for r in range(row):
        for c in range(col):
            if boards[r][c] == PERSON:
                return (r, c)

q = deque(fires)
while q:
    y, x = q.popleft()

    for dy, dx in delta:
        ny, nx = y + dy, x + dx

        if ny < 0 or ny >= row or nx < 0 or nx >= col:
            continue
        if boards[ny][nx] == WALL:
            continue
        if visited[ny][nx] >= 0:
            continue

        visited[ny][nx] = visited[y][x] + 1
        q.append((ny, nx))


def bfs(start):
    jVisited = [[-1 for _ in range(col)] for _ in range(row)]

    jVisited[start[0]][start[1]] = 0

    q = deque([start])
    while q:
        y, x = q.popleft()

        for dy, dx in delta:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= row or nx < 0 or nx >= col:
                return jVisited[y][x] + 1
            if boards[ny][nx] == WALL or jVisited[ny][nx] >= 0:
                continue
            if visited[ny][nx] != -1 and visited[ny][nx] <= jVisited[y][x] + 1:
                continue

            jVisited[ny][nx] = jVisited[y][x] + 1
            q.append((ny, nx))

    return 'IMPOSSIBLE'

print(bfs(findJ()))
