import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().strip())
stack, nums = [], []
d = {}

for i in range(n):
    x = input().strip()
    nums.append(x)

idx = 0
for i in range(len(arr)):
    if arr[i] != '*' and arr[i] != '/' and arr[i] != '+' and arr[i] != '-':
        if arr[i] not in d:
            d[arr[i]] = nums[idx]
            idx += 1

for i in range(len(arr)):
    if arr[i] == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif arr[i] == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif arr[i] == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif arr[i] == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    else:
        stack.append(float(d[arr[i]]))
print('%0.2f' % stack[0])
'''
파이썬으로 아스키코드 쓰는 법을 몰라서 아스키코드 쓸까 고민하다가
그냥 dictionary 를 썼다.
근데, ord 함수를 써서 아스키코드로 푼 사람들이 많은 것 같다.
아스키코드 사용하는 법도 알아놓자.
'''