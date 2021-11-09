import sys
import itertools
input = sys.stdin.readline

def gcd(a, b):
    return gcd(b, a % b) if b else a

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    sum = 0
    for a, b in itertools.combinations(arr, 2):
        sum += gcd(a, b)
    print(sum)