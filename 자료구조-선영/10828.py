import sys

def push(X):
    stack.append(X)
    
def pop():
    if len(stack)==0:
        return -1
    else:
        return stack.pop(-1)
    
def size():
    return len(stack)

def empty():
    if len(stack)!=0 :
        return 0
    else:
        return 1

def top():
    if(len(stack)==0):
        return -1
    else:
        return stack[-1]

n = int(sys.stdin.readline().rstrip())

stack=[]

for i in range(n):
    input_split = sys.stdin.readline().rstrip().split()
    order = input_split[0]
    
    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "top":
        print(top())
