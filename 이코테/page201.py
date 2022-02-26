n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
start = 0
end = max(arr)
total=0
while start <= end :
    ricecake=0
    mid = (start+end)//2
    for i in arr:
        if i > mid:
            ricecake =ricecake + (i-mid)
    if ricecake < m:
        end = mid-1
    else:
        total = mid
        start=mid+1
print(total)
