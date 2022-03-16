def solution(arr):
    number = 1
    cnt = 0
    while True:
        for i in arr:
            if number % i == 0:
                cnt = cnt+1
        if cnt == len(arr):
            return number
        number = number+1
        cnt = 0