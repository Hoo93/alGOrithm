import itertools


# 1 1 1 ~ 3 3 3 까지 출력 ( repeat 을 입력해줘야 함 )
for i in itertools.product([1, 2, 3], repeat=3):
    print(i)

# 조합 1~4 를 4C2 로 출력
for i in itertools.combinations([1, 2, 3, 4], 2):
    print(i)

# 순열 1~4 를 4P2 로 출력
for i in itertools.permutations([1, 2, 3, 4], 2):
    print(i)

for i in itertools.count(1):
    print(i)
    if i == 10:
        break


# pad 함수

target = '123'
print(target.zfill(5))  # 00123
print(target.rjust(5, 'Z'))  # ZZ123
print(target.ljust(5, 'Z'))  # 123ZZ


