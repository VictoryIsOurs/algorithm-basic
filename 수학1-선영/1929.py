#소수구하기

from sys import stdin

def find_primeNumber(n): #소수 찾기 (근데 시간 초과때문에 안씀!)
    if n ==1  :
        return False
    elif n== 2 :
        return True
    for i in range(2, int(n**0.5)+1): #n의 제곱근까지만 구해주면 됨. range(2,n) X
        if n % i == 0:
            return False
    return True

a,b = map(int, stdin.readline().split())  #시간 초과 문제 해결(!!!!!!!!!!!!!)

for n in range(a,b+1):
    if find_primeNumber(n):
        print(n)
