import sys


class SegmentTree:
    def __init__(self, numbers: [int]):
        self.numbers = numbers
        self.tree = [0 for _ in range(4 * len(numbers))]
        self.build(0, 0, len(numbers) - 1)

    # start, end 는 부분합을 구할 numbers 의 범위
    def build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = self.numbers[start]
        else:
            mid: int = (start + end) // 2

            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)

            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    # start, end, left, right 의 의미 찾기
    # start, end => numbers 배열의 시작 index, 마지막 인덱스
    # left, right 는 합을 구할 인덱스 ( left, right 를 포함한다 )
    def query(self, left: int, right: int):
        return self.__query_dfs(0, 0, len(self.numbers) - 1, left, right)

    def __query_dfs(self, node: int, start: int, end: int, left: int, right: int):
        if end < left or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2

        return (self.__query_dfs(2 * node + 1, start, mid, left, right) +
                self.__query_dfs(2 * node + 2, mid + 1, end, left, right))

    def update(self, targetIndex: int, value: int):
        self.__update_dfs(0, 0, len(self.numbers) - 1, targetIndex, value)

    def __update_dfs(self, node: int, start: int, end: int, targetIndex: int, value: int):
        if start == end:
            self.numbers[start] = value
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= targetIndex <= mid:
                self.__update_dfs(2 * node + 1, start, mid, targetIndex, value)
            else:
                self.__update_dfs(2 * node + 2, mid + 1, end, targetIndex, value)

            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    # format = cmd + opt + L


# file = open('input.txt', 'r')
# input = file.readline

input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
nums = [int(input()) for _ in range(N)]

segmentTree = SegmentTree(nums)
result = []

for _ in range(M + K):
    inst, argu_1, argu_2 = map(int, input().strip().split())
    if inst == 1:
        segmentTree.update(argu_1 - 1, argu_2)
    elif inst == 2:
        result.append(segmentTree.query(argu_1 - 1, argu_2 - 1))

for i in result:
    print(i)
