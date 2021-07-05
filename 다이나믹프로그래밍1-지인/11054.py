import sys
input = sys.stdin.readline

n = int(input())
A = [0] + list(map(int, input().split()))
dp1, dp2 = [0]*(n+1), [0]*(n+1)

dp1[1] = 1
for i in range(2, n+1):
    dp1[i] = 1
    for j in range(1, i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
dp2[n] = 1
for i in range(n-1, 0, -1):
    dp2[i] = 1
    for j in range(i+1, n+1):
        if A[i] > A[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
for i in range(1, n+1):
    dp1[i] += dp2[i] - 1
print(max(dp1))