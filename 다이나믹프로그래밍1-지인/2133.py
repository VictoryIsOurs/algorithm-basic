import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (31)
dp[2] = 3
for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * dp[2] + sum(dp[:i-2]) * 2 + 2 # sum(dp[:i-2]) * 2 여기서 *2 는 새로운 사각형
print(dp[n])