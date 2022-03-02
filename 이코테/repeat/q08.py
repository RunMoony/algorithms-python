s = input()
sum = 0
result = []
for i in s:
    if not i.isalpha():
        sum = sum + int(i)
    else: 
        result.append(i)
        result.sort()
result.append(sum)
for i in result:
    print(i,end="")