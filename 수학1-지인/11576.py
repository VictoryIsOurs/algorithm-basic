import sys
input = sys.stdin.readline

A, B = map(int, input().split())
m = int(input())
A_list = list(map(int, input().split()))

# A진법 수를 10진법으로 변환
A_to_dec = 0
for i in range(m):
    A_to_dec += A_list[i] * (A**(m-1-i))

# 10진법 수를 B진법으로 변환
B_list = []
while A_to_dec:
    B_list.append(A_to_dec % B)
    A_to_dec = A_to_dec // B

for i in reversed(range(len(B_list))):
    print(B_list[i], end=' ')