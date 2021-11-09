import sys
input = sys.stdin.readline

dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4
T = int(input())
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in range(T):
    n = int(input())
    print(dp[n])