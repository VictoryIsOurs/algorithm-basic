import sys
input = sys.stdin.readline

n = int(input())

num_list, stack, ans = [], [], []
arr = [i+1 for i in range(n)]
top = 0
flag = True

for i in range(n):
    num = int(input())
    num_list.append(num)

for i in range(n):
    target = num_list[i]
    for j in range(top, target):
        if arr[j] > 0:
            stack.append(arr[j])
            arr[j] = 0
            ans.append('+')
    top = stack.pop()
    if top == target:
        ans.append('-')
    else:
        flag = False
        print("NO")
        break
if flag:
    for i in range(len(ans)):
        print(ans[i])