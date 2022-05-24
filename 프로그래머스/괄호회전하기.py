def solution(s):
    answer = 0
    temp = list(s)
    for _ in range(len(s)):
        arr = []
        for i in range(len(temp)):
            if len(arr) >= 1:
                if arr[-1] == "[" and temp[i] == "]":
                    arr.pop()
                elif arr[-1] == "(" and temp[i] == ")":
                    arr.pop()
                elif arr[-1] == "{" and temp[i] == "}":
                    arr.pop()
                else:
                    arr.append(temp[i])
            else:
                arr.append(temp[i])
        if len(arr) == 0:
            answer+=1
        temp.append(temp.pop(0))
    return answer
                    