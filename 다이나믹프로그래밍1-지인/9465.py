import sys
input = sys.stdin.readline
t = int(input())
for k in range(t):
    n = int(input())
    a = []
    for i in range(2):
        a.append(list(map(int, input().split())))
    a[0][1] += a[1][0]
    a[1][1] += a[0][0]
    for j in range(2, n):
        a[0][j] += max(a[1][j-1], a[1][j-2])
        a[1][j] += max(a[0][j-1], a[0][j-2])
    print(max(a[0][n-1], a[1][n-1]))