/*
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

  괄호 문제
*/

import sys

n = int(input()) #이게 더 시간이 빨랐음. 

for k in range(n):

    stack=[]
    stack2=[]

    check = 1  # )가 먼저 나오는 경우를 체크하는 변수
    str = sys.stdin.readline()
    
    for i in str:
        if i =='(':
            stack.append(i)
        elif i==')':
            if(len(stack)!=0):
                stack.pop()
                
            else:
                check = 0

    if(len(stack)==0):
        if(check == 1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
