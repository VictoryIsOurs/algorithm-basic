import sys
import math
input = sys.stdin.readline

n = int(input())
m = []

for _ in range(n):
    m.append(list(map(int, input().split())))

res = math.inf

for k in range(3):
    dp = [[0 for i in range(n)] for j in range(3)]

    for i in range(3):
        if i == k:
            dp[i][0] = m[0][i]
            continue
        dp[i][0] = math.inf
        # 0번째 집을 R로 했을 때, dp[0][0]만 m[0][0] 이고 dp[1][0]과 dp[2][0]은 inf로 설정한다.
    for i in range(1, n):
        dp[0][i] = m[i][0] + min(dp[1][i-1], dp[2][i-1])
        dp[1][i] = m[i][1] + min(dp[0][i-1], dp[2][i-1])
        dp[2][i] = m[i][2] + min(dp[0][i-1], dp[1][i-1])

    for i in range(3):
        if i == k:
            continue
        res = min(res, dp[i][-1])
print(res)