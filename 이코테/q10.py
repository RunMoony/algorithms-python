#답안참고하였음

def rotated(key): #시계방향으로 90도 회전함수
    n = len(key) #행의 길이
    m = len(key[0]) #열의 길이
    result = [[0]* n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]

def check(new):
    lock_length = len(new)//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new[i][j] !=1:
                return False
    return True
        

def solution(key,lock):
    n = len(lock)
    m = len(key)
    new = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rotated(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new[x+i][y+j] += key[i][j]
                if check(new) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new[x+i][y+j] -= key[i][j]
    return False