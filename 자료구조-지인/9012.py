# 입력으로 주어진 괄호 문자열이 vps인지 아닌지 판단

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    sen = input()
    cnt = 0
    for j in range(len(sen)):
        if sen[j] == '(':
            cnt += 1
        elif sen[j] == ')':
            cnt -= 1

        if cnt < 0:
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")