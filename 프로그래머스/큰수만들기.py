## 시간 초과로 다시 풀기

from itertools import combinations

def solution(number, k):
    answer = list(number)
    cnt = [i for i in range(len(number))]
    per = list(combinations(cnt,(len(answer)-k)))
    result = []
    for i in per:
        a = ''
        for j in i:
            a = a + answer[j]
        result.append(a)
    return max(result)