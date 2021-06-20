#1676 팩토리얼 0의 갯수
from sys import stdin

def fact(n):
    sum = 1
    for i in range(1, n+1):
        sum = sum * i
    return sum


#n = int(input()) #런타임에러 발생
n = int(stdin.readline())
factorial_result = fact(n)


count = 0 

for i in reversed(list(str(factorial_result))): #str로 형변환, str거꾸로부터 확인
    if i== '0' :
        count +=1
    else:
        break

print(count)
