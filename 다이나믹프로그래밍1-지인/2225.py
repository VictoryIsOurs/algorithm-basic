'''
만약 n=20, k=5라면
20을 5개로 나눈 것
: [0+(20을 4개로 나눈 것)] + [1+(19를 4개로 나눈 것] + ... + [19+(1을 4개로 나눈 것)] + [20+(0을 4개로 나눈 것)]
dp[n][k] = dp[0][k-1] + dp[1][k-1] + ... + dp[n-1][k-1] + dp[n][k-1]
dp[n-1][k] = dp[0][k-1] + dp[1][k-1] + ... + dp[n-1][k-1]
dp[n][k] = dp[n-1][k] + dp[n][k-1]
'''
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0]*(k+1) for i in range(n+1)]
dp[0][0] = 1
for i in range(n+1):
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][k] % 1000000000)