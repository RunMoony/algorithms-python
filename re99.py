n,k = map(int, input().split())
cnt=0
while n != 1:
    if n % k ==0:
        n = n//k
        cnt=cnt+1
    else:
        n = n-1
        cnt=cnt+1
print(cnt)