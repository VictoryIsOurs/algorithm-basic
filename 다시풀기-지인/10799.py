import sys
input = sys.stdin.readline

ans = 0
stack = []
stick = list(input().strip())
for i, s in enumerate(stick):
    if s == '(':
        stack.append(i)
    else:
        if stack:
            if stack.pop() + 1 == i:
                ans += len(stack)
            else:
                ans += 1
print(ans)