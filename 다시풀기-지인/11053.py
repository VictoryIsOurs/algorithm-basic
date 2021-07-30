import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0] * 1001
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))