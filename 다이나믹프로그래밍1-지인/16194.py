import sys
N = int(sys.stdin.readline())
P = list(map(int, input().split()))
dp = [0] * 1001
for i in range(1, N+1):
    tmp = list()
    tmp.append(P[i-1])
    for j in range(1, i+1):
        tmp.append(dp[i-j] + P[j-1])
    dp[i] = min(tmp)
print(dp[N])