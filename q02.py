s = input()
result = int(s[0])
for i in range(1,len(s)):
    num = int(s[i])
    if result <= 1 or num <= 1:
        result = result + num
    else:
        result = result * num
print(result)