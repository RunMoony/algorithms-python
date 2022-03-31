from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for order in orders:
            temp+=combinations(sorted(order),i)
        count=Counter(temp)
        if count:
            if max(count.values()) >=2:
                for key,value in count.items():
                    if value == max(count.values()):
                        answer.append("".join(key))
    return sorted(answer)