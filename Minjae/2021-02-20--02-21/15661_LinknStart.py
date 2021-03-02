#WA
n= int(input())
abil= [[*map(int, input().split())] for _ in range(n)]

chk=[False]*n
ans=0
def play():
    global ans
    s=0
    l=0
    for i in range(n):
        for j in range(n):
            if chk[i] and chk[j]:
                s+=abil[i][j]
            elif not chk[i] and not chk[j]:
                l+=abil[i][j]
    ans= min(ans, abs(s-l))


def backtrack(i):
    if i==n:
        if any in chk:
            play()
        return
    chk[i]=True
    backtrack(i+1)
    chk[i]=False
    backtrack(i+1)

backtrack(0)
print(ans)