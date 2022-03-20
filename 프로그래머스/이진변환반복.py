def solution(s):
    num = 0
    delete_num = 0
    length = 0
    answer = []
    while True:
        for i in s:
            if i == "0":
                delete_num += 1 #제거할 0의 개수
            else: length += 1 #제거 후 길이
        s = str(format(length, 'b'))
        num += 1
        length = 0
        if s == "1" :
            break
    answer.append(num)
    answer.append(delete_num)
    return answer