n= int(input())
mp= [["*"]*n for _ in range(n)]

def rec(y, x, r):
    side=r//3
    for i in range(y+side,y+2*side):
        for j in range(x+side,x+2*side):
            mp[i][j]=' '
    if side==1:
        return
    rec(y, x, r//3)
    rec(y, x+side, r//3)
    rec(y, x+2*side, r//3)
    rec(y+side, x, r//3)
    rec(y+side, x+2*side, r//3)
    rec(y+2*side, x, r//3)
    rec(y+2*side, x+side, r//3)
    rec(y+2*side, x+2*side, r//3)
rec(0,0,n)
[print(''.join(el)) for el in mp]