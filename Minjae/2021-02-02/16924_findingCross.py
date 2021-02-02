n, m= map(int, input().split())

mp= [[' ']*(m+2)]
mp+= [[' ']+list(input())+[' '] for _ in range(n)]
mp+= [[' ']*(m+2)]

dy= [1, -1, 0, 0]
dx= [0, 0, 1, -1]

def cross(i, j, d):
    isCross=True
    for y, x in zip(dy, dx):
        if mp[i+y*d][j+x*d] == '#' or mp[i+y*d][j+x*d] == '*':
            continue
        else:
            isCross= False
            break
    return isCross 

def chk(i, j, d):
    for y, x in zip(dy, dx):
        mp[i+y*d][j+x*d]= '#'

ans=[]
for i in range(1, n+1):
    for j in range(1,m+1):
        if mp[i][j]=='*' or mp[i][j]=='#':
            for k in range(1, 100+1):
                if cross(i, j, k):
                    mp[i][j]='#'
                    chk(i, j, k)
                    ans.append((i, j, k))
                    continue
                else:
                    break
possi=True
for i in range(1, n+1):
    for j in range(1,m+1):
        if mp[i][j]=='*':
            possi= False

#[print(*el) for el in mp]
if possi:
    print(len(ans))
    [print(*el) for el in ans]
else:
    print(-1)

