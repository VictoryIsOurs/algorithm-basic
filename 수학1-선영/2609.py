#최대공약수와 최소공배수

import sys

n1, n2 = map(int, input().split())

#유클리드 호제법 사용
a, b= n1, n2
while b != 0:
    a = a%b    #예: 6 = 24%18
    a,b = b,a  #swap

print(a) #최대공약수 출력

print(n1*n2//a) #최소공배수 출력
