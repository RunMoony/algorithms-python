n, m = map(int, input().split())
data = list(map(int, input().split(" ")))
arr = [0]*11

for x in data:
    arr[x] = arr[x]+1 #무게별 개수

result = 0
for i in range(1,m+1):
    n = n-arr[i]
    result += arr[i] * n