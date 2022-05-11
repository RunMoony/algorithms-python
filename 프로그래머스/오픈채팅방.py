def solution(record):
    answer = []
    dict= {}

    for i in record:
        split = i.split()
        if len(split) == 3:
            dict[split[1]] = split[2]
    for i in record:
        split = i.split()
        if split[0] == "Enter":
            answer.append('%s님이 들어왔습니다.'%dict[split[1]])
        if split[0] == "Leave":
            answer.append('%s님이 나갔습니다.'%dict[split[1]])
    return answer
