import sys

sys.setrecursionlimit(10000)

# f = open('input.txt', 'r')
# input = f.readline
input = sys.stdin.readline

MAX = 10001


N,M = map(int, input().split())
board = [[MAX for _ in range(M+2)]]+[[MAX] + list(map(int, input().split())) + [MAX] for _ in range(N)]+[[MAX for _ in range(M+2)]]
visited = [[-1 for _ in range(M+2)] for _ in range(N+2)]

delta = [(-1,0),(1,0),(0,-1),(0,1)]

# visited 체크
# 더 낮은 숫자인지 확인
# 더 낮은 숫자가 아닌 경우 return 0
# 더 낮은 숫자인 경우 visited[y][x] += dfx(ny,nx)
def dfs(y,x):
    # 이미 방문한 경우 처리
    if visited[y][x] != -1:
        return visited[y][x]
    # 종점에 도착한 경우 처리
    if y == N and x == M:
        return 1
    # 처음 도착한 경우 초기화
    visited[y][x] = 0

    for dy,dx in delta:
        ny,nx = y+dy,x+dx
        if board[ny][nx] >= board[y][x]:
            continue
        visited[y][x] += dfs(ny,nx)

    return visited[y][x]

dfs(1,1)

print(visited[1][1])
