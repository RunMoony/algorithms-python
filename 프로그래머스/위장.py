from collections import defaultdict

def solution(clothes):
    answer = 1
    dict = defaultdict(list)
    for i in clothes:
            dict[i[1]].append(i[0])
    key = dict.keys()
    for i in key:
        answer = answer * (len(dict[i]) + 1)
    return answer-1