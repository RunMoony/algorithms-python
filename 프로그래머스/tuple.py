def solution(s):
    s = s[2:-2]
    s = s.split("},{")
    s = sorted(s, key= lambda x : len(x))    
    answer = []
    result = []
    for i in s:
        a = i.split(',')
        answer.append(a)
    for j in answer:
        for z in j:
            if not z in result:
                result.append(z)
    result = list(map(int,result))
    return result