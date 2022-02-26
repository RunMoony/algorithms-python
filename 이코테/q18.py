#올바른 괄호 문자열 인지 판단
def check_good(p):
    cnt=0
    for i in p:
        if i == "(":
            cnt+=1
        else:
            if cnt == 0:
                return False
            cnt-=1
    return True

#균형잡힌 괄호 문자열
def seperate(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else: cnt -=1
    if cnt == 0:
        return i

def solution(p):
    answer = ""
    if p == "":
        return answer
    index = seperate(p)
    u = p[:index+1]
    v = p[index + 1:]
    
    if check_good(u):
        return u + solution(v)
    else:
        answer="("
        answer += solution(v)
        answer += ")"
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
    return answer




        