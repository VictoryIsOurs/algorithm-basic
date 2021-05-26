import sys
input = sys.stdin.readline

stack1, stack2 = list(input())[:-1], []
m = int(input())

for i in range(m):
    commend = list(input().split())
    if commend[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
        else:
            pass
    elif commend[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
        else:
            pass
    elif commend[0] == 'B':
        if stack1:
            stack1.pop()
        else:
            pass
    else:
        stack1.append(commend[-1])

print(''.join(stack1) + ''.join(stack2[::-1]))
