n,m,k = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
cnt = 0
sum = 0
first = arr[n-1]
second = arr[n-2]
while True:
    for i in range(k):
        if m == cnt :
            break
        else:
            sum=sum+first
            cnt=cnt+1
    if m == cnt:
        break
    sum = sum+second
    cnt=cnt+1
print(sum)