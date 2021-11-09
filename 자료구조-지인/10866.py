import sys
input = sys.stdin.readline

n = int(input())
dq = []
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        dq.insert(0, cmd[1])
    elif cmd[0] == 'push_back':
        dq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if dq:
            print(dq.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if dq:
            print(dq.pop(-1))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)