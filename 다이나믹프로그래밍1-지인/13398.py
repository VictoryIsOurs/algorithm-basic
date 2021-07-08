import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n)]
dp[0] = [A[0], -1000]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + A[i], A[i]) # 특정 원소를 제거하지 않은 경우
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + A[i]) # 특정 원소를 제거한 경우

ans = -1000
for i in range(n):
    ans = max(ans, max(dp[i]))
print(ans)