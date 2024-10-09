import sys

from collections import deque

# format = cmd + opt + L

# file = open('input.txt', 'r')
# input = file.readline

input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]

M, N = map(int, input().strip().split())
board = [input() for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]

visited[0][0] = 0
q = deque([(0, 0)])

while q:
    y, x = q.popleft()

    for dy, dx in delta:
        ny, nx = y + dy, x + dx

        if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
        if 0 <= visited[ny][nx] <= visited[y][x] + (board[ny][nx] == '1'):
            continue

        visited[ny][nx] = visited[y][x] + (board[ny][nx] == '1')
        q.append((ny, nx))

print(visited[N - 1][M - 1])
