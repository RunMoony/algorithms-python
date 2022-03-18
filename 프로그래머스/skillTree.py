def solution(skill, skill_trees):
    word = ""
    cnt = 0
    arr = []
    for i in skill_trees:
        for j in i:
            if j in skill:
                word+=j
        if word == "":
            cnt = cnt+1
        arr.append(word)
        word = ""
    for i in arr:
        if (i in skill) and (skill[0] in i):
            cnt = cnt+1
    return cnt