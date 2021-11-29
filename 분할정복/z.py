import sys

result = 0
def div_n_con(n, x, y):
    global result

    if x == r and y == c:
        print(result)
        exit(0)

    # 좌표가 속하지 않는 사각형을 통으로 거른다.
    if not (x <= r < x+n and y <= c < y+n):
        result += n*n
        return

    div_n_con(n//2, x, y)
    div_n_con(n//2, x, y+n//2)
    div_n_con(n//2, x+n//2, y)
    div_n_con(n//2, x+n//2, y+n//2)

n, r, c = map(int, sys.stdin.readline().split())
div_n_con(2**n, 0, 0)