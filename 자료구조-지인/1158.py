import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = [i for i in range(1, n+1)]
ans = []
idx = 0

for i in range(0, n):
    idx += k-1
    if idx >= len(q):
        idx = idx % len(q)
    ans.append(str(q.pop(idx)))
print('<',', '.join(ans), '>', sep='')