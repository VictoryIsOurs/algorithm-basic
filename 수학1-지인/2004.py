import sys
input = sys.stdin.readline

n, m = map(int, input().split())
def count(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

print(min((count(n, 2) - count(m, 2) - count(n-m, 2)), (count(n, 5) - count(m, 5) - count(n-m, 5))))

'''
8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
8 = 2 x 2 x 2
6 = 2 x 3
4 = 2 x 2
2 = 2 x 1

8!에서 2가 나오는 횟수는 7번이다.
1. 2로 나누어 떨어지는 수의 개수를 구한다. 8 / 2 = 4
2. 2 * 2로 나누어 떨어지는 수의 개수를 구한다. 8 / (2 * 2) = 2
3. 2 * 2 * 2로 나누어 떨어지는 수의 개수를 구한다. 8 / (2 * 2 * 2) = 1
따라서 4 + 2 + 1 = 7
'''