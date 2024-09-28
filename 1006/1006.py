import sys

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

testCase = int(input())
col, soldiers = map(int, input().split())

upper = list(map(int, input().split()))
lower = list(map(int, input().split()))


def getABC(start_a: int, start_b: int, start_c: int):
    # i-1 열까지 1,2 행을 모두 채우는 최소값 // 근데 왜 i-1 열까지지 ?
    a = [0 for _ in range(col + 1)]
    # i 열까지 1 행을 모두 채우고 2 행은 1행은 i-1 열까지 채웠을 때 최소값
    b = [0 for _ in range(col + 1)]
    # i 열까지 2 행을 모두 채우고 1 행은 2행은 i-1 열까지 채웠을 때 최소값
    c = [0 for _ in range(col + 1)]

    a[0], b[0], c[0] = start_a, start_b, start_c
    for i in range(1, col + 1):
        a[i] = min(c[i-1]+1, b[i - 1] + 1)
        # upper lower 조건문 로직 수정 필요함
        if upper[i - 1] + upper[i] <= soldiers:
            a[i] = min(a[i], c[i - 1] + 1)
        if lower[i - 1] + lower[i] <= soldiers:
            a[i] = min(a[i], b[i - 1] + 1)
        if upper[i] + lower[i] <= soldiers:
            a[i] = min(a[i], a[i - 1] + 1)

        b[i] = a[i] + 1
        if upper[i] + lower[i] <= soldiers:
            b[i] = min(b[i], c[i - 1] + 1)

        c[i] = a[i] + 1
        if lower[i - 1] + lower[i] <= soldiers:
            c[i] = min(c[i], b[i - 1] + 1)

    a[col] = min(a[col - 1], b[col - 1] + 1)
    if upper[col - 1] + upper[i] <= soldiers:
        a[i] = min(a[i], c[i - 1] + 1)
    if lower[i - 1] + lower[i] <= soldiers:
        a[i] = min(a[i], b[i - 1] + 1)
    if upper[i] + lower[i] <= soldiers:
        a[i] = min(a[i], a[i - 1] + 1)

    return [a, b, c]


# 1 0~ N-1 , N ~ 2N-1 이 모두 연결되지 않은 경우
result = getABC(0, 1, 1)[0][col]

if upper[col - 1] + upper[0] <= soldiers:
    result = min(getABC(0, 0, 1)[2][col - 1] + 1, result)

if lower[col - 1] + lower[0] <= soldiers:
    result = min(getABC(0, 1, 0)[1][col - 1] + 1, result)

if upper[col - 1] + upper[0] <= soldiers and lower[col - 1] + lower[0] <= soldiers:
    result = min(getABC(0, 1, 1)[1][col - 2] + 2, result)

sys.stdout.write(result)
sys.stdout.flush()
