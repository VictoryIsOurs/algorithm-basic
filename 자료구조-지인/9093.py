import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    input_list = input().split()
    for word in input_list:
        print(word[::-1], end=' ')