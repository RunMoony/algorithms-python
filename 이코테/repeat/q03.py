S = input()
cnt0 = 0
cnt1 = 0
if S[0] == '0':
    cnt1 = 1
else: cnt0 = 1
for i in range(1,len(S)):
    if S[i] != S[i-1]:
        if S[i] == '0':
            cnt1 += 1
        else: cnt0 += 1
print(min(cnt0, cnt1))