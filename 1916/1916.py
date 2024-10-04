import sys
import heapq

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

INF = 1e9
# input = sys.stdin.readline

cityCount = int(input())
busCount = int(input())

costs = [INF for _ in range(cityCount + 1)]

# edges[start] = (const, end)[]
edges = [[] for _ in range(cityCount + 1)]

for _ in range(busCount):
    start, end, cost = map(int, input().strip().split())
    edges[start].append((cost, end))

startCity, endCity = map(int, input().strip().split())

# 시작 지점 초기화
costs[startCity] = 0

# 우선순위 큐 초기화
pq = [(0, startCity)]

while pq:
    cost, currentCity = heapq.heappop(pq)

    if cost > costs[currentCity]:
        continue

    for eCost, end in edges[currentCity]:
        if cost + eCost < costs[end]:
            costs[end] = cost + eCost
            heapq.heappush(pq, (cost + eCost, end))

print(costs[endCity])
