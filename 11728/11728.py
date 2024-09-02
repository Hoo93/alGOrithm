import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))

result = []

while a and b:
    if a[0] <= b[0]:
        result.append(a.popleft())
    else:
        result.append(b.popleft())

if len(a) > 0:
    result += a
else:
    result += b

print(' '.join(map(str, result)))