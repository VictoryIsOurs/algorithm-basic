# 최소공배수

# 유클리드 호제법을 사용한다.
# 유클리드 호제법 : a를 b로 나눈 나머지를 r이라고 했을 때, a와 b의 최대공약수는 b와 r의 최대공약수이다.

# 유클리드 호제법을 통해서 계산한 최대공약수로 최소공배수 구하기
# a = G * x, b = G * y -> x와 y는 서로소
# a * b = G * G * x * y
# 최소공배수 = G * x * y = a * b // G
import sys
input = sys.stdin.readline

def gcd(a, b):
    return gcd(b, a % b) if b else a
def lcm(a, b):
    return a * b // gcd(a, b)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))