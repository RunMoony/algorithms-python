n = int(input())
x,y = 1,1
plan = input().split()

for i in plan :
    if i=='L' and y!=1 : y=y-1
    if i=='R' and y!=n : y=y+1
    if i=='U' and x!=1 : x=x-1
    if i=='D' and x!=n : x=x+1 

    if x>n : x=x-1
    if y>n : y=y-1



print(x,y)
