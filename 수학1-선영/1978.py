#소수찾기

def find_primeNumber(n):
    if n ==1  :
        return False
    elif n== 2 :
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

j = 0
count_sosu = 0

n = int(input()) #첫줄에 수의 개수 N이 주어진다.

numlist = list(map(int, input().split() ))  #얘 위치 잘 두기!!!!!(얘 위치 헷갈려서 시간 잡음 ㅠ)


for i in numlist:
    if(find_primeNumber( i ) == True):
       count_sosu += 1

    j+=1

print(count_sosu)


