# 소수 구하기
# 에라토스테네스의 체
import sys
input = sys.stdin.readline

prime = [True] * 1001
prime[0], prime[1] = False, False

def find_prime():
    m = 1000 // 2
    for i in range(2, m+1):
        if prime[i] == True:
            for j in range(i+i, 1001, i):
                prime[j] = False

t = int(input())
num_list = list(map(int, input().split()))
find_prime()
sum = 0

for num in num_list:
    if prime[num] == True:
        sum += 1
print(sum)