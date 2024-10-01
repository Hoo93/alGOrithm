import sys

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

N, S = map(int, input().strip().split())
result = 0

nums = sorted(map(int, input().strip().split()))


def backTracking(index: int, sum: int):
    # 파이썬은 글로벌 변수를 읽는 것은 가능 N,S,nums
    # 글로벌 변수에 값을 쓰려고 하면 로컬 변수 취급함
    # 그렇기 때문에 global 지정해줘야함
    global result
    if index == N and sum == S:
        result += 1
    if index >= N:
        return
    if sum > S and nums[index] > 0:
        return

    backTracking(index + 1, sum)
    backTracking(index + 1, sum + nums[index])


backTracking(0, 0)

if S == 0:
    result -= 1
print(result)
