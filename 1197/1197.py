import sys
import heapq

# f = open('input.txt', 'r')
# input = f.readline
input = sys.stdin.readline

V, E = map(int, input().split())
# 1~V 까지 V 개의 정점이 존재
edges = [[] for _ in range(V + 1)]
result = 0

# 간선 세팅 (value, node)
for _ in range(E):
    node1, node2, value = map(int, input().split())
    edges[node1].append((value, node2))
    edges[node2].append((value, node1))

# 방문한 노드 확인
issued = set()

# 1번 노드를 처음으로 방문한다고 가정
issued.add(1)
# 우선순위 큐 : value 를 기준으로 오름차순으로 정렬
pq = []
for edge in edges[1]:
    heapq.heappush(pq, edge)

while len(issued) < V:
    value, node = heapq.heappop(pq)
    if issued.__contains__(node): continue

    result += value
    issued.add(node)
    for edge in edges[node]:
        heapq.heappush(pq, edge)

print(result)
