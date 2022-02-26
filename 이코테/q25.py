n = int(input())
stages = list(map(int, input().split()))
length = len(stages)
arr = []
for i in range(1, n+1):
    count = stages.count(i)

    if length ==0:
        fail = 0
    else:
        fail = count/length
    
    arr.append((i,fail))
    length = length-count

arr = sorted(arr,key=lambda x:x[1], reverse=True)
answer = []
for i in arr:
    answer.append(i[0])
print(answer)