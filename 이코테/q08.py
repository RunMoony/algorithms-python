s = input()
arr = []
sum=0
for i in range(len(s)):
    if ord(s[i]) < 65:
        sum = sum+int(s[i])
    else: arr.append(s[i])
arr = sorted(arr)
arr.append(sum)
for i in arr:
    print(i, end="")
