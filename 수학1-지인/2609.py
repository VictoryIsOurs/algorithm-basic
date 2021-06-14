inputs = list(map(int, input().split()))
a, b = inputs[0], inputs[1]
while(a!=b):
    if(a>b): a-=b
    else: b-=a
print(a)
print((int)(a*(inputs[0]/a)*(inputs[1]/a)))