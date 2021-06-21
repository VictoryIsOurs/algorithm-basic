#최소공배수

def gcd(a, b): #최대 공약수 구하는 함수

    A, B = a, b
    #유클리드 호제법 사용
    while B != 0:
        A = A%B
        A, B = B, A #SWAP

    return A
        
def lcm(a, b): #최소공배수 구하는 함수
    GCD = gcd(a,b)

    return a*b//GCD



n = int(input())

i = 0
while( i<n):
    a,b = map(int, input().split())
    print(lcm(a,b))
    i+=1
   
