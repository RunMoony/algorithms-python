def solution(operations):
    arr = []
    result = []
    for i in operations:
        arr.append(i.split(" "))
    for i in arr:
        if i[0] == "I":
            result.append(int(i[1]))
        if i[0] == "D" and result != []:
            if i[1] == "1":
                result.remove(max(result))
            if i[1] == "-1":
                result.remove(min(result))
    if result == []:
        return [0,0]
    else: return [int(max(result)),int(min(result))]