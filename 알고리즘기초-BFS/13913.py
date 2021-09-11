#숨바꼭질

from collections import deque

 
INF = 100000

N, K= map(int, input().split())

dist = [0]*(INF+1)

path = [0]*(INF+1)

 

def solve_bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        if x == K:
            print(dist[x])
            p = []

            while x != N:
                p.append(x)
                x = path[x]

            p.append(N)

            p.reverse()

            print(' '.join(map(str, p)))

            return

        for nx in (x*2,x-1, x+1):

            if 0 <= nx <= INF and not dist[nx]:

                dist[nx] = dist[x]+1

                path[nx] = x

                q.append(nx)

 

 

solve_bfs()
