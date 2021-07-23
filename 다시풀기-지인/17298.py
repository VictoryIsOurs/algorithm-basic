import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
ans = [-1] * n
stack = []

for i in range(n):
    while stack and (stack[-1][0] < A[i]):
        tmp, idx = stack.pop()
        ans[idx] = A[i]
    stack.append([A[i], i])
print(*ans)

# 아이디어가 어렵다.
# 2중 for문을 없애고 스택 하나로만 운용 하려하니 더 어려운 것 같다.