n = int(input())
arr = []
for i in range(n):
    a = input().split(" ")
    arr.append(a)
arr = sorted(arr, key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])