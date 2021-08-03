
n = int(input())

#dp 로 푸는 문제임
# n>3 일때, f(n) = f(n-1) + f(n-2) + f(n-3)이 나옴. 

def solution(n):
    if n == 1 :
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return solution(n-3) + solution(n-2) + solution(n-1)

for _ in range(n):
    print(solution(int(input())))

            
