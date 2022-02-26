n,k = map(int, input().split()) #n:원소개수 k:최대 바꿔치기
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a) #오름차순
b = sorted(b ,reverse=True)
cnt = 0
for i in range(n) :
    if a[i] < b[i] :
        a[i],b[i] = b[i],a[i]
        cnt = cnt+1
    if cnt == k:
        break
print(sum(a))