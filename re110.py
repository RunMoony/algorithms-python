n = int(input())
dir = list(input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
x,y=1
move = ['L','R','U','D']
for i in dir:
    for j in range(4):
        if i == move[j] :
            nx = x+dx[j]
            ny = y+dx[j]
    if nx < 1 or ny < 1 or nx>n or ny>n:
        continue
    x = nx
    y = ny
print(x,y)
