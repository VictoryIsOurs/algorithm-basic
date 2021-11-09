import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))
order = max(dp)
ans = []
for i in range(N-1, -1, -1):
    if dp[i] == order:
        ans.append(A[i])
        order -= 1
ans.reverse()
print(*ans)