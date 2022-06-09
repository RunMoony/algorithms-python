## 시간 초과로 다시 풀기

from itertools import combinations

## 내 코드
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

## 참고한 코드

def solution(number,k):
    answer = []
    for num in number:
        while answer and k>0 and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    answer = ''.join(answer[:len(number)-k])
    return answer