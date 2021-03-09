n = int(input())
maps = [list(input()) for _ in range(n)]
ans = 0

def check() :
    global ans
    for i in range(n) :
        cnt = 1
        for j in range(1,n) :
            if maps[i][j] == maps[i][j-1] :
                cnt += 1
            else :
                ans = max(ans ,cnt)
                cnt = 1

        ans = max(ans, cnt)
    
    for i in range(n) :
        cnt = 1
        for j in range(1,n) :
            if maps[j][i] == maps[j-1][i] :
                cnt += 1
            else :
                ans = max(ans, cnt)
                cnt = 1

        ans = max(ans, cnt)

for i in range(n) :
    for j in range(n-1) :
        temp = maps[i][j] 
        maps[i][j] = maps[i][j+1]
        maps[i][j+1] = temp

        check()

        temp = maps[i][j+1]
        maps[i][j+1] = maps[i][j]
        maps[i][j] = temp

        #############################

        temp = maps[j][i]
        maps[j][i] = maps[j+1][i]
        maps[j+1][i] = temp

        check()

        temp = maps[j+1][i]
        maps[j+1][i] = maps[j][i]
        maps[j][i] = temp

print(ans)