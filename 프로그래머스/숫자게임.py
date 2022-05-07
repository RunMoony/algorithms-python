def solution(A, B):
    answer = 0
    index = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in A:
        if i >= B[index]:
            continue
        else:
            answer+=1
            index+=1
    return answer