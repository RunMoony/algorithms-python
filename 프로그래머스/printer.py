def solution(priorities, location):
    cnt = 0
    while True:
        max_num = max(priorities)
        for i in range(len(priorities)):
            if max_num == priorities[i]:
                priorities[i] = 0
                max_num = max(priorities)
                cnt += 1
                if i == location:
                    return cnt