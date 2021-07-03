import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i-1, 0, -1):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(max(dp))