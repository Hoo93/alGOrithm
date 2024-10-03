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

# dict
mem = dict([('a', 1), ('b', 2), ('c', 3)])
print(mem.keys())
print(mem.values())
print(mem.items())

mem['d'] = 4

print(mem.popitem())  # ('d', 4) 가장 최근에 삽입한 값 반환
print(mem.pop('a'))
print(mem.popitem())

# set // add remove
s = set([2, 1, 3])
s.add(4)
s.add(-1)

s.remove(2)
for i in s:
    print(i)

s2 = set([3, 4, 5])
print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))

# set 속성이 tuple 인 경우
s3 = set([(1, 2), (3, 4), (5, 6)])
s3.add((1, 2))
for i in s3:
    print(i)

print(s3.__contains__((1, 2)))

# set 속성이 list 인 경우 // 애초에 불가능 ( unhashable )
s4 = set([[1, 2], [3, 4], [5, 6]])
s4.add([1, 2])
for i in s4:
    print(i)
