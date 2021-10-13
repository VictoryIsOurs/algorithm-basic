def OX():

    H, M = map(int, input().split(" "))

    if M > 44: #걍 45분 이상일때
        print(H, M-45)
    elif M < 45 and H > 0 :  #3: 30
        print(H-1,60 - (45-M))
    else: #H == 0 일때
        print(23,M+15)
if __name__ == '__main__':
    OX()
