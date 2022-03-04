def solution(s):
    compressed = []
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2 +1):
        cnt = 1
        str = ""
        for j in range(0,len(s),i):
            a = s[j:j+i]
            b = s[j+i:j+2*i]
            if a == b:
                cnt = cnt+1
            else:
                if cnt!=1:
                    str += (str(cnt) + a)
                else:
                    str += a
                cnt = 0
        compressed.append((str,len(str)))
    compressed.sort(key=lambda x:(x[1]))
    return compressed[0][1]
