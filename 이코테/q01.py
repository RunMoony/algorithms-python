from re import S


n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
cnt = 0
result = 0
for i in arr:
    cnt = cnt+1
    if cnt >= i:
        result = result+1
        cnt = 0
print(result)
    

