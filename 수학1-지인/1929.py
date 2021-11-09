import sys
input = sys.stdin.readline

m, n = map(int, input().split())
prime = [1]*1000001
# 0 : 소수 아님
# 1 : 소수
prime[0], prime[1] = 0, 0
for i in range(n+1):
    if prime[i] == 1:
        for j in range(i+i, n+1, i):
            prime[j] = 0

for i in range(m, n+1):
    if prime[i] == 1:
        print(i)