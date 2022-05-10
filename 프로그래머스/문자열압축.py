def solution(s):
    answer = []
    for i in range(1,len(s)//2+1):
        compressed = ""
        prev = s[0:i]
        cnt = 1
        for j in range(i,len(s),i):
            if prev == s[j:j+i]:
                cnt+=1
            else:
                if cnt!=1:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                prev = s[j:j+i]
                cnt = 1
        if cnt >=2:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        answer.append(len(compressed))
    return min(answer)
