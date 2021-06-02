# 2중 for 문 => 시간초과

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

# print(*리스트) 하면, 띄어쓰기가 된 채로 리스트의 원소가 출력된다.