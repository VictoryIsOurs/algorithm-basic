import sys
import copy

input = sys.stdin.readline

N, M, K = map(int, input().split())
dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
grid = [[[] for i in range(N)] for j in range(N)]
    
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    grid[r-1][c-1].append((m, s, d))
    
for k in range(K):
    new_grid = [[[] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                while grid[i][j]:
                    fireball = grid[i][j].pop(0)
                    m, s, d = fireball[0], fireball[1], fireball[2]
                    nx, ny = (i+dir[d][0]*s)%N, (j+dir[d][1]*s)%N
                    new_grid[nx][ny].append((m, s, d))
    grid = copy.deepcopy(new_grid)

    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) >= 2:
                tmp = []
                nm, ns, nd = 0, 0, 0
                odd_dir, even_dir = 0, 0
                
                for u in grid[i][j]:
                    nm += u[0]
                    ns += u[1]
                    nd = u[2]
                    if nd%2 == 0: even_dir += 1
                    else: odd_dir += 1
                
                nm //= 5
                ns //= len(grid[i][j])
                if (not odd_dir and even_dir and nm) or (odd_dir and not even_dir and nm): 
                    tmp += [(nm, ns, 0), (nm, ns, 2), (nm, ns, 4), (nm, ns, 6)]
                elif odd_dir and even_dir and nm: 
                    tmp += [(nm, ns, 1), (nm, ns, 3), (nm, ns, 5), (nm, ns, 7)]
                    
                grid[i][j] = copy.deepcopy(tmp)

ans = 0
for i in range(N):
    for j in range(N):
        if len(grid[i][j]):
            for u in grid[i][j]:
                ans += u[0]
print(ans)
