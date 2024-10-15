import sys

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

INF = 1e9

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]

# [min, max]
segment_tree = [[INF, 0] for _ in range(4 * N)]


def init(node, start, end):
    if start == end:
        segment_tree[node] = [nums[start], nums[start]]
    else:
        mid = (start + end) // 2

        init(2 * node + 1, start, mid)
        init(2 * node + 2, mid + 1, end)

        segment_tree[node][0] = min(segment_tree[2 * node + 1][0], segment_tree[2 * node + 2][0])
        segment_tree[node][1] = max(segment_tree[2 * node + 1][1], segment_tree[2 * node + 2][1])


def solve(node, start, end, left, right):
    if left > end or right < start:
        return [INF, 0]
    # 이 부분을 실수함
    elif start >= left and end <= right:
        # elif start < left and right < end: 기존 코드
        return segment_tree[node]
    else:
        mid = (start + end) // 2

        mn1, mx1 = solve(2 * node + 1, start, mid, left, right)
        mn2, mx2 = solve(2 * node + 2, mid + 1, end, left, right)
        return [min(mn1, mn2), max(mx1, mx2)]


init(0, 0, N - 1)

for _ in range(M):
    mn, mx = map(int, input().split())
    result = solve(0, 0, N - 1, mn - 1, mx - 1)
    print(result[0], result[1])
