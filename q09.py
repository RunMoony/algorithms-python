def solution(s):
    arr = []
    if len(s) == 1:
        return 1
    for cut in range(1,(len(s)//2)+1):
        cnt = 1
        result=""
        for i in range(0,len(s),cut):
            first = s[i:i+cut]
            second = s[i+cut:i+2*cut]
            if first == second:
               cnt = cnt+1
            else:
                if cnt != 1:
                    result += str(cnt)+first
                else:
                    result += first
                cnt = 1
        arr.append((result,len(result)))
    arr = sorted(arr, key=lambda x:x[1])

    return arr[0][1]