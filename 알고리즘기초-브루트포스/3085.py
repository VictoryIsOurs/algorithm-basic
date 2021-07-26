# 사탕게임
from sys import stdin
n = int(stdin.readline())
arr = []
re = 0
for i in range(n):
    arr.append(list(stdin.readline().strip()))
# print(arr)
    
def check():
    # 행
    cnt1 = 1
    cnt2 = 1
    ans = 0
    for i in range(n):
        for j in range(n-1):
            # 행
            if(arr[i][j]==arr[i][j+1]):
                cnt1+=1
            else:
                cnt1=1
            ans =max(ans,cnt1)
            #열
            if(arr[j][i]==arr[j+1][i]):
                    cnt2+=1
            else:
                cnt2=1
            ans =max(ans,cnt2)
    return ans

# 위치를 교환 할때마다 check 해야함
for i in range(n-1):
    for j in range(n-1):
        # 오른쪽
        arr[i][j],arr[i][j+1] =arr[i][j+1],arr[i][j] # 오른쪽 바꾸기
        re = max(re,check())
        arr[i][j+1],arr[i][j] =arr[i][j],arr[i][j+1] # 다시바꾸기
        # 아래 
        arr[j][i],arr[j+1][i] =arr[j+1][i],arr[j][i] # 아래바꾸기
        re = max(re,check())
        arr[j+1][i],arr[j][i] =arr[j][i],arr[j+1][i] # 다시바꾸기
print(re)
