import sys

# format = cmd + opt + L

# file = open('input.txt', 'r')
# input = file.readline

input = sys.stdin.readline

INF = 1e9

N = int(input())
M = int(input())

costs = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    startCity, endCity, cost = map(int, input().strip().split())

    if costs[startCity - 1][endCity - 1] > cost:
        costs[startCity - 1][endCity - 1] = cost

for i in range(N):
    costs[i][i] = 0

for mid in range(N):
    for start in range(N):
        for end in range(N):
            costs[start][end] = min(costs[start][end], costs[start][mid] + costs[mid][end])

for i in range(N):
    costs[i] = [0 if cost >= INF else cost for cost in costs[i]]

for i in costs:
    print(' '.join(map(str, i)))
