import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*4 for _ in range(n+1)]
h = [[0]*4 for _ in range(n+1)]

for i in range(1, n+1):
    h[i][1], h[i][2], h[i][3] = map(int, input().split())

dp[1] = h[1]
for i in range(2, n+1):
    dp[i][1] = min(dp[i-1][2] + h[i][1], dp[i-1][3] + h[i][1])
    dp[i][2] = min(dp[i-1][1] + h[i][2], dp[i-1][3] + h[i][2])
    dp[i][3] = min(dp[i-1][1] + h[i][3], dp[i-1][2] + h[i][3])
print(min(dp[n][1:]))
