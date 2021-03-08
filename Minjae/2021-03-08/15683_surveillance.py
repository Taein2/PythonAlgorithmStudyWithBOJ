from sys import *; setrecursionlimit(100000)
# dir 위 오 아 왼
dir= [(-1,0), (0,1), (1,0), (0,-1)]


n, m= map(int, input().split())
mp= [[-1]*(m+2)]
mp+=[[-1]+[*map(int, input().split())]+[-1] for _ in range(n)] 
mp+= [[-1]*(m+2)]

# 6은 벽

cctv= []
for i in range(1,n+1):
    for j in range(m+1):
        if mp[i][j]>0 and mp[i][j]<6:
            cctv.append((i,j,mp[i][j]))

Len= len(cctv)
mn=1e9

tst= [mp[i][:] for i in range(len(mp))]
def run(i, j,direct):
    global tst
    y= direct[0]
    x= direct[1]
    #print(i,j)
    if tst[i+y][j+x]>=0 and tst[i+y][j+x]!=6:
        tst[i+y][j+x]=7
        run(i+y, j+x, direct)
    else:
        return 
    


def CHK():
    global tst
    sm=0
    #[print(*el) for el in tst]
    #print()
    for i in range(1,n+1):
        for j in range(m+1):
            if tst[i][j]==0:
                sm+=1
    return sm

chk= [[[False]*6 for _ in range(5)] for _ in range(Len)]


#[print(*el) for el in cctv]

def backtrack(i, todo):
    #print(i)
    global tst
    #[print(*el) for el in tst]
    #print()
    if i==Len:
        global mn
        for Y, X, DIR in todo:
            run(Y,X,DIR)
        mn= min(mn,CHK())
        tst= [mp[i][:] for i in range(len(mp))]
        return

    ts= cctv[i]
        #print(ts)
        
    if ts[2]==1:
        
        for k in range(4):
            if not chk[i][1][k]:
                chk[i][1][k]=True
                todo.append((ts[0], ts[1], dir[k]))
                backtrack(i+1,todo)
                todo.pop()
                chk[i][1][k]=False
    if ts[2]==2:
        for k in range(2):
            if not chk[i][2][k]:
                chk[i][2][k]=True
                todo.append((ts[0], ts[1], dir[k]))
                todo.append((ts[0], ts[1], dir[k+2]))
                backtrack(i+1,todo)
                todo.pop()
                todo.pop()
                chk[i][2][k]=False
    if ts[2]==3:
        for k in range(4):
            if not chk[i][3][k]:
                chk[i][3][k]=True
                todo.append((ts[0], ts[1], dir[k]))
                todo.append((ts[0], ts[1], dir[(k+1)%4]))
                backtrack(i+1,todo)
                todo.pop()
                todo.pop()
                chk[i][3][k]=False
    if ts[2]==4:
        for k in range(4):
            if not chk[i][4][k]:
                chk[i][4][k]=True
                todo.append((ts[0], ts[1], dir[k]))
                todo.append((ts[0], ts[1], dir[(k+1)%4]))
                todo.append((ts[0], ts[1], dir[(k+2)%4]))
                backtrack(i+1,todo)
                todo.pop()
                todo.pop()
                todo.pop()
                chk[i][4][k]=False
    if ts[2]==5:
        for v in range(4):
            todo.append((ts[0], ts[1], dir[v]))
        backtrack(i+1,todo)
        for _ in range(4):
            todo.pop()
        


backtrack(0,[])
print(mn)






