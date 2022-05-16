def solution(phone_book):
    answer = []
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i == j:
                continue
            if phone_book[i] in phone_book[j]:
                answer.append(1)
            else:
                answer.append(0)
    if 1 in answer:
        return False
    if not 1 in answer:
        return True