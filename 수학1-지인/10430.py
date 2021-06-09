inputs = list(map(int, input().split()))
a, b, c = inputs[0], inputs[1], inputs[2]
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)