import sys
from collections import deque

MAX = 10 ** 5 #시간 초과 안나게 미리 설정
dist = [0] * (MAX+1) #이동하는 거리를 알기 위한 변수 distance
n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft() #n값
        if x == k :
            print(dist[x])
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx]=dist[x]+1
                q.append(nx)

bfs()
