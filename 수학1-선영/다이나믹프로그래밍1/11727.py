n=int(input())
dp=[1,3,5]
if(n>3):
    for i in range(3,n):
        dp.append(dp[i-1]*2+1)
print(dp[n-1])
