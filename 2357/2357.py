import sys

# format = cmd + opt + L

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

N,M = map(int, input().split())

nums = [ int(input()) for _ in range(N) ]

for _ in range(M):
    mn, mx = map(int, input().split())