s = input()
make0 = 0
make1 = 0

if s[0] == '0':
    make1 = make1 + 1
else :
    make0 = make0  + 1
for i in range(len(s)-1):
    if s[i] != s[i+1] :
        if s[i+1] == '0' :
            make1 = make1+1
        else: make0 = make0+1
print(min(make0,make1))