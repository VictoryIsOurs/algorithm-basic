import sys

stack = []
cnt = 0
a = sys.stdin.readline().strip()

for i in range(len(a)):
    if a[i] == '(':
        stack.append('(')
    else:
        if a[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)