import sys

f = open('../input.txt', 'r')
input = f.readline

# input = sys.stdin.readline

N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

delta = [(-1,0),(1,0),(0,-1),(0,1)]

for dx,dy in delta:
    print(dx,dy)
