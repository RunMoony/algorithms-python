n = int(input())
level = list(map(int, input().split(" ")))
level.sort()
result = 0
cnt = 0

for i in level:
    cnt = cnt+1
    if cnt >= i:
        result = result+1
        cnt = 0
print(result)