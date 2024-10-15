import sys

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

INF = 1e9

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]

# [min, max]
segment_tree = [[INF, 0] for _ in range(4*N)]


def init(node, start, end):
    if start == end:
        segment_tree[node] = [nums[start], nums[start]]
    else:
        mid = (start + end) // 2

        init(2 * node + 1, start, mid)
        init(2 * node + 2, mid + 1, end)

        segment_tree[node][0] = min(segment_tree[2 * node + 1][0], segment_tree[2 * node + 2][0])
        segment_tree[node][1] = max(segment_tree[2 * node + 1][1], segment_tree[2 * node + 2][1])


init(0, 0, N - 1)

print(segment_tree)

for _ in range(M):
    mn, mx = map(int, input().split())
