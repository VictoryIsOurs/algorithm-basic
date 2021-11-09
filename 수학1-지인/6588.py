import sys
input = sys.stdin.readline

prime = [True] * 1000001
prime[0], prime[1] = False, False

def find_prime():
    m = 1000000 // 2
    for i in range(2, m+1):
        if prime[i] == True:
            for j in range(i*2, 1000001, i):
                prime[j] = False
find_prime()

while(True):
    flag = False
    n = int(input())
    if n == 0:
        break
    for i in range(3, n):
        if prime[i] == True and prime[n-i] == True and i % 2 == 1 and (n-i) % 2 ==1:
            print(n, '=', i, '+', n-i)
            flag = True
            break
    if flag == False:
        print("Goldbach's conjecture is wrong.")