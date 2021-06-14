import sys
input = sys.stdin.readline

S = input().strip()
ans = ''
stack = []
for s in S:
    if ord(s) >= ord('A') and ord(s) <= ord('Z'):
        ans += s
    else:
        if s == '(':
            stack.append(s)
        elif s == ')':
            while stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(s)
        else:
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(s)
while stack:
    ans += stack.pop()
print(ans)