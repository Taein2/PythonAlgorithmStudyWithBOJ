n= int(input())
mp=[ [*map(int, input().split())] for _ in range(n)]

chk= [False]*n
chk[0]=True
mn=3000

def add():
    s=0
    t=0
    for i in range(n):
        for j in range(n):
            if chk[i] and chk[j]:
                s+=mp[i][j]
            elif not chk[i] and not chk[j]:
                t+=mp[i][j]
            
    return abs(s-t)

def backtrack(i,cnt):
    global mn
    if cnt+n-i<2//n-1:
        return
    if i>=n:
        return
    chk[i]=True
    cnt+=1
    if cnt==n//2-1:
        mn= min(mn,abs(add()))
    backtrack(i+1,cnt)
    chk[i]=False
    backtrack(i+1,cnt-1)
    


backtrack(1,0)
print(mn)

