import math

def solution(progresses, speeds):
    arr = []
    for i in range(len(progresses)):
        n = math.ceil((100-progresses[i])/speeds[i])
        arr.append(n)
    answer = [1]
    for i in range(1,len(arr)):
        if arr[i-1] >= arr[i]:
            answer[len(answer)-1] = answer[len(answer)-1]+1
        else: answer.append(1)
    return answer