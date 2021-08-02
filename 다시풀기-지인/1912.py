import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
total = [a[0]]
for i in range(n-1):
    total.append(max(total[i] + a[i+1], a[i+1]))
print(max(total))
