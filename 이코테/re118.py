n,m = map(int, input().split())
result = []

for i in range(n):
    result.append([0]*m)

x,y,direction = map(int, input().split())
result[x][y] = 1

array=[]
for i in range(n) :
    array.append(list(map(int, input().split())))

dx = [-1,0,1,0] #북동남서
dy = [0,1,0,-1]

def turnleft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
cnt=1
turn=0
while True:
    turnleft()
    nx = x+dx[direction]
    ny = y+dy[direction]
    if array[nx][ny] == 0 and result[nx][ny] == 0:
        result[nx][ny] = 1
        turn=0
        cnt+=1
        continue
    else:
        turn+=1
    if turn == 4:
        nx=x-dx[direction]
        ny=y-dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else: break
print(cnt)