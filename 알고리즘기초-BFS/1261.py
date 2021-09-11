#어렵
#다시 풀기 

#알고스팟
import sys
import heapq

INF = sys.maxsize

x = [0,0,-1,1]
y = [-1,1,0,0]

n,m = map(int, sys.stdin.readline().split())

visited = [[0 for _ in range(n)]for _ in range(m)]
graph = []
dist = [[INF for _ in range(n)] for _ in range(m)]
for i in range(m):
    temp = list(input())
    temp = [int(i) for i in temp]
    graph.append(temp)

heap = []
heapq.heappush(heap, [graph[0][0],[0,0]])
while heap:
    cost, now = heapq.heappop(heap)
    visited[now[0]][now[1]] = 1
    if dist[now[0]][now[1]] > cost:
        dist[now[0]][now[1]] = cost
        if now[0] == m - 1 and now[1] == n - 1:
            break
    else:
        continue
    for i in range(4):
        if 0<=now[0]+x[i]<m and 0<=now[1]+y[i]<n and visited[now[0]+x[i]][now[1]+y[i]] == 0:
            if dist[now[0]+x[i]][now[1]+y[i]] > cost + graph[now[0]+x[i]][now[1]+y[i]]:
                heapq.heappush(heap, [cost+graph[now[0]+x[i]][now[1]+y[i]], [now[0]+x[i],now[1]+y[i]]])

print(dist[m-1][n-1])
