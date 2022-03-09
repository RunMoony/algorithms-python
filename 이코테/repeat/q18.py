def balance(p): #균형잡힌 괄호 문자열 만들기
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0 :
            return i

def check_proprer(p): #올바른 괄호 문자열인지 판단
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -=1
        return True

def solution(p):
    result = ""
    if p == "":
        return result
    index = balance(p)
    u = p[:index+1]
    v = p[index+1:]
    if check_proprer(u):
        result = u + solution(v)
    else :
        result = '('
        result += solution(v)
        result += ')'
        for i in range(1,len(u)-1):
            if u[i] == '(':
                u[i] = ')'
            else: u[i] = '('
        result+=u
    return result




    return answer
