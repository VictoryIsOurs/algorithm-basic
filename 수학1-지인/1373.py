import sys
input = sys.stdin.readline

# int()에 ,를 찍고 숫자를 넣으면 그 진법의 숫자를 받는다.
print(oct(int(input(), 2))[2:])