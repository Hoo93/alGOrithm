import sys

file = open('input.txt', 'r')
input = file.readline

# input = sys.stdin.readline

testCase = int(input())
col, soldiers = map(int, input().split())

upper = list(map(int, input().split()))
lower = list(map(int, input().split()))

