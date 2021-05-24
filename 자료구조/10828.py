# 스택
import sys
input = sys.stdin.readline

stack = []
# push : stack.append(4)
# pop : top = stack.pop() -> 제거한 원소를 리턴 받는다.
# top : stack[-1]

n = int(input())

for i in range(n):
    input_list = input().split()
    if input_list[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif input_list[0] == "size":
        print(len(stack))
    elif input_list[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif input_list[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(input_list[1])