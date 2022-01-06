n = int(input())
num = []
for i in range(n) :
    num.append(int(input()))

result = sorted(num,reverse=True)

for i in range(len(result)) :
    print(result[i], end=' ')
