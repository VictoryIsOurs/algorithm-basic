import sys
input = sys.stdin.readline

N, B = input().split()
alpha = {}
base = 'A'
for i in range(10, 36):
    alpha[base] = i
    base = chr(ord(base)+1)

ans = 0
for i in range(len(N)):
    if ord(N[i]) >= ord('A') and ord(N[i]) <= ord('Z'):
        ans += alpha[N[i]]*(int(B)**(len(N)-i-1))
    else:
       ans += int(N[i])*(int(B)**(len(N)-i-1))
print(ans)