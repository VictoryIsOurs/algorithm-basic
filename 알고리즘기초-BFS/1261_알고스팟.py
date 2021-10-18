import sys
from collections import deque
#BFS 벽을 최소 몇개 부숴야 하는가???
def OX():
    #열, 행
    n, m = map(int, sys.stdin.readline().split()) #(N,M)으로 이동하기 위해
    a=[]

    for i in range(m): #벽들을 다 받아준다.
        a.append(sys.stdin.readline())

    #dist - 가중치
    dist =[[-1]*n for _ in range(m)] #dist를 다 -1로 채워주기

    dist[0][0] = 0 #빈방이다

    q = deque()
    dx=[1,-1,0,0] #이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다.
    dy=[0,0,1,-1] #이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다.
    q.append([0,0])

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx>=0 and nx<m and ny>=0 and ny <n: #범위안에 있으면
                if dist[nx][ny] == -1: #방문한 적이 없는데
                    if a[nx][ny] == '0': #빈 방이면
                        q.appendleft([nx, ny])
                        dist[nx][ny]=dist[x][y]
                    elif a[nx][ny] == '1': #벽이 있다면
                        q.append([nx,ny])
                        dist[nx][ny] = dist[x][y]+1

    print(dist[m-1][n-1])


if __name__ == '__main__':
    OX()



