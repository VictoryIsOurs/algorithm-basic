import sys
input = sys.stdin.readline

N, B = map(int, input().split())
alpha = {}
base = 'A'
for i in range(10, 36):
    alpha[i] = base
    base = chr(ord(base)+1)

ans = ''
while N:
    if (N % B) >= 10:
        ans += alpha[N % B]
    else:
        ans += str(N % B)
    N = N // B
print(ans[::-1])