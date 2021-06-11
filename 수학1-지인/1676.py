import sys
input = sys.stdin.readline

N = int(input())

def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return n * 1
    return n * fact(n-1)

def zero(cnt, n):
    if n % 10 != 0:
        return cnt
    return zero(cnt+1, n // 10)

print(zero(0, fact(N)))
