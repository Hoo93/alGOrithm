import sys
import heapq

# format = cmd + opt + L

INF = 1e9

# file = open('input.txt', 'r')
# input = file.readline

input = sys.stdin.readline
while True:

    N, M = map(int, input().strip().split())

    if N == 0 and M == 0:
        break

    S, D = map(int, input().strip().split())

    edges = [[] for _ in range(N)]
    costs = [INF for _ in range(N)]

    for _ in range(M):
        U, V, cost = map(int, input().strip().split())
        edges[U].append((V, cost))

    # (누적 코스트, 위치)
    pq = [(0, S)]
    costs[S] = 0

    shortestPath = [set() for _ in range(N)]
    while pq:
        accumulatedCost, node = heapq.heappop(pq)

        if accumulatedCost > costs[node]:
            continue

        for dest, cost in edges[node]:
            newCost = accumulatedCost + cost
            if newCost == costs[dest]:

                shortestPath[dest] = shortestPath[dest].union(shortestPath[node])
                shortestPath[dest].add((node, dest, cost))
            elif newCost < costs[dest]:
                costs[dest] = newCost

                shortestPath[dest] = shortestPath[node].copy()
                shortestPath[dest].add((node, dest, cost))

                heapq.heappush(pq, (newCost, dest))

    for i in range(N):
        tmp = []
        for d, c in edges[i]:
            if not shortestPath[D].__contains__((i, d, c)):
                tmp.append((d, c))
        edges[i] = tmp

    costs = [INF for _ in range(N)]

    # (누적 코스트, 위치)
    pq = [(0, S)]
    costs[S] = 0

    while pq:
        accumulatedCost, node = heapq.heappop(pq)

        if accumulatedCost > costs[node]:
            continue

        for dest, cost in edges[node]:
            if accumulatedCost + cost < costs[dest]:
                costs[dest] = accumulatedCost + cost

                heapq.heappush(pq, (accumulatedCost + cost, dest))

    if costs[D] >= INF:
        print(-1)
    else:
        print(costs[D])
