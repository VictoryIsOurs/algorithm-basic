import sys
input = sys.stdin.readline

N, S = map(int, input().strip().split())
As = list(map(int, input().strip().split()))

def gcd(a, b):
    return gcd(b, a % b) if b else a

dist = []
for i in range(N):
    dist.append(abs(As[i]-S))

ans = dist[0]
for i in range(1, N):
    ans = gcd(ans, dist[i])


print(ans)