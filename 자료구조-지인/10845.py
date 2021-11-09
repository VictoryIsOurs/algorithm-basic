import sys
input = sys.stdin.readline

n = int(input())

queue = []

for i in range(n):
    input_list = input().split()
    if input_list[0] == 'push':
        queue.append(int(input_list[1]))
    elif input_list[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif input_list[0] == 'size':
        print(len(queue))
    elif input_list[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif input_list[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)