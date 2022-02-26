def solution(food_times, k):
    answer = 0
    time = 0
    i=0
    while True: 
        if food_times[i] == 0:
            i=i+1
        else : 
            food_times[i] = food_times[i]-1
            time = time + 1
            i = i+1
        if time == k:
            if i>=len(food_times):
                i = i-len(food_times)
                answer = food_times[i]
                return answer
        if i == len(food_times):
            i = 0

food_times = list(map(int,input().split()))
k = int(input())
print(solution(food_times,k))