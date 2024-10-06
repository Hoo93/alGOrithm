import sys
import heapq
import bisect

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

N, K = map(int, input().split())

# 보석의 무게와 가치
jewels = []
bags = []
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(jewels, (weight, value))

for _ in range(K):
    bags.append(int(input()))

bags.sort()

answer = 0
issued = [False for _ in range(K)]

available_jewels = []
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        weight, value = heapq.heappop(jewels)
        heapq.heappush(available_jewels,-value)

    if available_jewels:
        nValue = heapq.heappop(available_jewels)
        answer -= nValue

print(answer)


# 틀린 첫 풀이
#
#
#issued = [False for _ in range(K)]
#
#while jewels:
#    value, weight = heapq.heappop(jewels)
#    idx = bisect.bisect_left(bags, weight)
#
#    if idx >= K: continue
#
#    이 부분에서 최악의 경우 K 를 탐색하므로 시간 복잡도가 NK 가 될 수 있음
#    while idx < K and issued[idx]:
#        idx += 1
#
#    if idx < K:
#        issued[idx] = True
#        answer -= value
#
#print(answer)
###
