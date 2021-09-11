
s = int(input())

MAX = 999999999
time = [[MAX for i in range(1001)] for j in range(1001)]

# 1, 0
def bfs(s, c):
    q = [[s, c]]
    time[s][c] = 0
    while q:
        now = q.pop(0)
        s_now = now[0]
        c_now = now[1]
        if time[s_now][s_now] == MAX:
            time[s_now][s_now] = time[s_now][c_now] + 1
            q.append([s_now, s_now])
        if s_now + c_now <= 1000 and time[s_now + c_now][c_now] == MAX:
            time[s_now + c_now][c_now] = time[s_now][c_now] + 1
            q.append([s_now + c_now, c_now])
        if s_now - 1 >= 0 and time[s_now - 1][c_now] == MAX:
            time[s_now - 1][c_now] = time[s_now][c_now] + 1
            q.append([s_now - 1, c_now])
bfs(1, 0)
print(min(time[s]))
