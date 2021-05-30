#import 잊지 말기!!
from collections import deque 
import sys


#deque 선언
dq = deque()

n = int(sys.stdin.readline())

for j in range(n):
    str = sys.stdin.readline().split()

    if(str[0] =='push_back'):
        dq.append(str[1])

    elif(str[0]=='push_front'):
        dq.appendleft(str[1])

    elif(str[0]=='pop_front'):
        if(len(dq)==0):
            print("-1")
        else:
            tmp = dq.popleft()
            print(tmp)
            #print(dq.popleft())를 해주면 -1이 출력되므로, tmp에 저장 후 출력하기!

    elif(str[0]=='pop_back'):
        if len(dq)==0 :
            print("-1")
        else:
            tmp = dq.pop() 
            print(tmp)
            #print(dq.pop())를 해주면 -1이 출력되므로, tmp에 저장 후 출력하기!

    elif(str[0]=='front'):
        if(len(dq)==0):
            print("-1")
        else:
            print(dq[0]) #popleft를 쓰면 안됨! front는 그냥 print해주면 됨

    elif(str[0]=='back'):
        if(len(dq) ==0):
            print("-1")
        else:
            print(dq[len(dq)-1])

    elif(str[0]=='size'):
        print(len(dq))    
        
    elif(str[0]=='empty'):
        if(len(dq)==0):
            print("1")
        else:
            print("0")
            
