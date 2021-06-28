import sys
input = sys.stdin.readline

n = int(input())
ans = ''

if not n:
    print(0)
    exit()

while n:
    if n < 0:
        ans += str((-n) % 2)
        n = (-n+1)//2
    elif n > 0:
        ans += str(n % 2)
        n = -(n//2)
print(ans[::-1])