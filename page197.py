def search(find,arr,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == find:
            return mid
        elif arr[mid] > find:
            end = mid-1
        else :
            start = mid+1
    return None

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
arr1 = sorted(arr1)

for i in arr2:
    result = search(i,arr1,0,n-1)
    if result!=None:
        print('yes',end=' ')
    else: print('no', end=' ')