example = ["aeiou","abcdf","kfgcd","aaabc","abefg","abefk"] 
answer = []
mo = ["a","e","i","o","u"]
for i in example:
    cnt1 = 0
    cnt2 = 0
    same = 0
    seq = 1
    first = i[0]
    seqword = ord(i[0])
    for j in i: 
        if j == first:
            same += 1
        else:
            same = 0
            fisrt = j
        if j in mo:
            cnt1 += 1
            cnt2 = 0
        if j not in mo:
            cnt2 += 1
            cnt1 = 0
        if same >=3 or cnt1 >= 4 or cnt2 >=4 :
            break
    for k in range(1,len(i)):
        if seqword + 1 == ord(i[k]):
            seq += 1
            seqword = ord(i[k])
        else:
            seq = 1
            seqword = ord(i[k])
        if seq >=3:
            break
    if cnt1 >=4 or cnt2 >=4 or same>=3 or seq>=3 :
        answer.append(0)
    else:
        answer.append(1)
print(answer)
