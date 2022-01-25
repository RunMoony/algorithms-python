n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)

num = 1
for i in arr:
    if num < i:
        break
    num+=i
print(num)