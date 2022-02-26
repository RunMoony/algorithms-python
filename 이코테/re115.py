data = input()
a = int(ord(data[0])-96)
b = int(data[1])
step = [(-2,-1),(-2,1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]
cnt = 0
for i in step :
    nx = a+i[0]
    ny = b+i[1]
    if nx<1 or nx>8 or ny<1 or ny>8:
        continue
    cnt = cnt+1
print(cnt)

