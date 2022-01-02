data = input()
r = int(data[1])
c = int(ord(data[0])) - 96
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,2),(1,2),(1,-2),(-1,-2)]

result = 0
for step in steps :
    next_r = r + step[0]
    next_c = c + step[1]
    if next_c >=1 and next_c<=8 and next_r >=1 and next_r <=8 : 
        result += 1

print(result)