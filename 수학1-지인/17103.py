import sys
input = sys.stdin.readline

MAX = 1000001
prime = [1]*MAX # 0은 소수 아님, 1은 소수임
prime[0], prime[1] = 0, 0

for i in range(MAX):
    if prime[i] == 1:
        for j in range(i+i, MAX, i):
            prime[j] = 0

def gold(N):
    cnt = 0
    for i in range(1, N//2 + 1):
        if prime[i] == 1 and prime[N-i] == 1:
            cnt += 1
    return cnt

T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    print(gold(N))