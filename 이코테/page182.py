n,k = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1 = sorted(arr1)
arr2 = sorted(arr2, reverse=True)
sum=0
cnt=0
for i in range(n):
    if arr1[i] < arr2[i]:
        arr1[i] = arr2[i]
        cnt = cnt+1
    if cnt>=k:
        break

for i in range(len(arr1)):
    sum = sum+arr1[i]
print(sum)