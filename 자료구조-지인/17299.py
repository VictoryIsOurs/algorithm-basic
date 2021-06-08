import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
stack, ans = [], [-1]*n

freq = [0]*(1000001)
for i in range(n):
    freq[A[i]] += 1

for i in range(n):
    while stack and (freq[stack[-1][0]] < freq[A[i]]):
        a, idx = stack.pop()
        ans[idx] = A[i]
    stack.append([A[i], i])
print(*ans)