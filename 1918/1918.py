import sys

#file = open('input.txt', 'r')
#input = file.readline

input = sys.stdin.readline

operatorStack = []

answer = ''
for char in input():
    if char == '(':
        operatorStack.append(char)
    elif char == ')':
        while operatorStack and operatorStack[-1] != '(':
            answer += operatorStack.pop()
        operatorStack.pop()
    elif char == '*' or char == '/':
        while operatorStack and (operatorStack[-1] == '*' or operatorStack[-1] == '/'):
            answer += operatorStack.pop()
        operatorStack.append(char)
    elif char == '+' or char == '-':
        while operatorStack and operatorStack[-1] != '(':
            answer += operatorStack.pop()
        operatorStack.append(char)
    else:
        answer += char.strip()


while operatorStack:
    answer += operatorStack.pop()

print(answer)


