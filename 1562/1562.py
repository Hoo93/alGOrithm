import sys

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

N = int(input())

dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N)]

for i in range(1,10):
    dp[0][i][1<<i] = 1

for i in range(1,N):
    # 도착 지점이 0 인 경우
    # 도착 지점이 9 인 경우
    # 도착 지점이 1~8 인 경우
    for j in range(1,9):
        # dp[i][j][0 ~ 1023]
        for k in range(1024):
            dp[i][j][k | (1<<j)] += dp[i-1][j-1][k]
            dp[i][j][k | (1<<j)] %= 1000000000
            dp[i][j][k | (1<<j)] += dp[i-1][j+1][k]
            dp[i][j][k | (1<<j)] %= 1000000000

    for k in range(1024):
        dp[i][0][k | 1<<0] += dp[i-1][1][k]
        dp[i][0][k | 1<<0] %= 1000000000
        dp[i][9][k | 1<<9] += dp[i-1][8][k]
        dp[i][9][k | 1<<9] %= 1000000000

answer = 0
for i in range(10):
    answer += dp[N-1][i][1023]
    answer %= 1000000000

print(answer)


