def solution(n, words):
    arr = []
    arr.append(words[0])
    cnt = 0
    ok = 1
    for i in range(1,len(words)):
        cnt = cnt+1
        num = cnt//n
        if (words[i-1][-1] != words[i][0]) or (words[i] in arr) :
            answer = (i+1)%n
            if answer == 0:
                answer = n
            return [answer,num+1]
        else: ok += 1
        if ok == len(words):
            return [0,0]
        arr.append(words[i])