# N * N 크기의 정사각형 공간. 1 * 1 크기의 정사각형으로 이루어짐.
# (1,1) -> (N,N) 의 좌표로 이루어져있으며 시작좌표는 항상 1,1이다.
# L : 왼쪽으로 한 칸 이동 
# R : 오른쪽으로 한 칸 이동
# U : 위쪽으로 한 칸 이동
# D : 아래쪽으로 한 칸 이동
# 좌표를 벗어나는 움직임은 무시된다.
# 
# 입력조건 : 첫째줄에는 공간의 크기 N
#           둘쨰줄에는 이동할 계획서 내용이 주어진다.
# 출력 조건 : 최종적으로 도착할 지점의 좌표를 (X,Y)를 공백으로 구분하여 출력한다.
# EX)
# 5
# R R R U D D
# 3 4

x, y = 1, 1
n = int(input())
plans = input().split()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
nx, ny = 0, 0
action = ['L','R','U','D']

for plan in plans :
    for i in range(len(action)) :
        if plan == action[i] :
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny >n :
            continue
        x,y = nx,ny
print(x,y)

        
