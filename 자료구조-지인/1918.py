import sys
input = sys.stdin.readline

S = list(input())
stack = []

for i in range(len(S)):
    if ord(S[i]) >= ord('A') and ord(S[i]) <= ord('Z'):
        print(S[i])
    if S[i] == '+' or S[i] == '-':
        if not stack:
            while stack:
                print(stack.pop())
        stack.append(S[i])
    elif S[i] == '*' or S[i] == '/':
        if not stack:
            idx = -1
            while stack[idx] == '*' and stack[idx] == '/':
                print(stack.pop())
                idx -= 1
        stack.append(S[i])
    elif S[i] == '(':
        stack.append(S[i])
    elif S[i] == ')':
        idx = -1
        while True:
            if stack[idx] == '(':
                break
            print(stack.pop())
            idx -= 1
while stack:
    print(stack.pop())