def solution(prices):
    answer = []
    while prices != []:
        cnt = 0
        price = prices.pop(0)
        for i in range(len(prices)):
            if price <= prices[i]:
                cnt += 1
        answer.append(cnt)
    return answer