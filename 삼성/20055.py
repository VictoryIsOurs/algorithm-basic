import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
belt = list(map(int, input().strip().split()))
robot = [0]*len(belt) # 로봇이 있는 위치를 나타낸다.
cnt = 1

while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt = [belt[-1]] + belt[:len(belt)-1] # 벨트 회전
    robot = [robot[-1]] + robot[:len(robot)-1] # 로봇 회전
    robot[N-1] = 0 # 로봇이 내리는 위치에 있으면 로봇 내리기
        
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0: # 1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
    robot[N-1] = 0 # 로봇이 내리는 위치에 있으면 로봇 내리기
        
    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if not robot[0] and belt[0] > 0:
        belt[0] -= 1
        robot[0] = 1
    
    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if belt.count(0) >= K:
        print(cnt)
        break
    cnt += 1