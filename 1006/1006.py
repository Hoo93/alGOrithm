import sys

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

testCase = int(input())


def solve(start, a, b, c):
    for i in range(start, col):
        a[i + 1] = min(c[i] + 1, b[i] + 1)
        # 이 두 조건문 필요 없음 위의 조건식에 이미 포함된 내용이기 때문 !
        # if upper[i - 1] + upper[i] <= soldiers:
        #     a[i] = min(a[i], c[i - 1] + 1)
        # if lower[i - 1] + lower[i] <= soldiers:
        #     a[i] = min(a[i], b[i - 1] + 1)

        if upper[i] + lower[i] <= soldiers:
            a[i + 1] = min(a[i + 1], a[i] + 1)
        # a[i] 는 i-1열 까지 다 채우는 경우이기 때문에 upper, lower 에 들어가는 index 주의해야함
        if i > 0 and upper[i] + upper[i - 1] <= soldiers and lower[i] + lower[i - 1] <= soldiers:
            a[i + 1] = min(a[i + 1], a[i - 1] + 2)

        if i < col - 1:
            b[i + 1], c[i + 1] = a[i + 1] + 1, a[i + 1] + 1
            if upper[i + 1] + upper[i] <= soldiers:
                b[i + 1] = min(b[i + 1], c[i] + 1)

            if lower[i + 1] + lower[i] <= soldiers:
                c[i + 1] = min(c[i + 1], b[i] + 1)

    return a, b, c

for _ in range(testCase):
    col, soldiers = map(int, input().split())

    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))

    # i-1 열까지 1,2 행을 모두 채우는 최소값 // 근데 왜 i-1 열까지지 ?
    a = [0 for _ in range(col + 1)]
    # i 열까지 1 행을 모두 채우고 2 행은 1행은 i-1 열까지 채웠을 때 최소값
    b = [0 for _ in range(col + 1)]
    # i 열까지 2 행을 모두 채우고 1 행은 2행은 i-1 열까지 채웠을 때 최소값
    c = [0 for _ in range(col + 1)]

    # 1 0~ N-1 , N ~ 2N-1 을 모두 연결하지 않은 경우
    a[0], b[0], c[0] = 0, 1, 1
    a, b, c = solve(0, a, b, c)

    # 0열 과 N-1 열의 연결이 없을 때의 a[col] => col-1 열까지를 모두 채웠을 때의 최소 값
    result = a[col]

    # 1행 0열과 N-1열을 연결했다고 가정했을 때 //
    if col > 1 and upper[col - 1] + upper[0] <= soldiers:
        # 1행 0열과 1행 N-1열이 없다고 가정하고 초기 세팅
        a[0], b[0], c[0] = 0, 0, 1
        # b[1] = 2 인 이유는 c[0] + 1
        a[1], b[1] = 1, 2
        c[1] = 1 if lower[0] + lower[1] <= soldiers else 2
        # 1열 까지는 세팅했기 때문에 start 값을 1로 줌
        a, b, c = solve(1, a, b, c)

        # 1행 0열과 N-1열을 연결했기 때문에 2행 N-1열 까지만 채우고 + 1 (1행 0열과 N-1열) 해주면 됨
        result = min(result, c[col - 1] + 1)

    # 2행 0열과 1행 N-1열을 연결했다고 가정
    if col > 1 and lower[col - 1] + lower[0] <= soldiers:
        # 2행 0열과 1행 N-1열이 없다고 가정하고 초기 세팅
        a[0], b[0], c[0] = 0, 1, 0
        # c[1] = 2 인 이유는 b[0] + 1
        a[1], c[1] = 1, 2
        b[1] = 1 if upper[0] + upper[1] <= soldiers else 2
        # 1열 까지는 세팅했기 때문에 start 값을 1로 줌
        a, b, c = solve(1, a, b, c)

        # 2행 0열과 N-1열을 연결했기 때문에 1행 N-1열 까지만 채우고 + 1 (2행 0열과 N-1열) 해주면 됨
        result = min(result, b[col - 1] + 1)

    # 1,2행 모두 0열,N-1열을 연결했다고 가정
    if col > 1 and upper[col - 1] + upper[0] <= soldiers and lower[col - 1] + lower[0] <= soldiers:
        # 1,2행 0열과 1,2행 N-1열이 없다고 가정하고 초기 세팅
        a[0], b[0], c[0] = 0, 0, 0
        a[1], b[1], c[1] = 0, 1, 1
        # 1열 까지는 세팅했기 때문에 start 값을 1로 줌
        a, b, c = solve(1, a, b, c)

        # 1,2행 0열과 N-1열을 연결했기 때문에 N-2 열 까지 모두 채운 후 + 2 를 해주면 됨
        result = min(result, a[col - 1] + 2)

    print(result)
