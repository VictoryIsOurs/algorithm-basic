import sys
def OX():
    n = int(sys.stdin.readline())
    cnt = 0
    for j in range(n):
        num_list = list(map(int,input().split(' ')))
        avg = sum(num_list[1:])/num_list[0]
        result = 0
        cnt = 0
        #평균을 넘는 애들 반올림.
        for i in num_list[1:]:
            if i > avg:
                cnt += 1
        result = (cnt / num_list[0]) *100
        print(f'{result:.3f}%')


if __name__ == '__main__':
    OX()
