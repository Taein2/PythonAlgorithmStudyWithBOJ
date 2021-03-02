sq= [[*map(int, input().split())] for _ in range(3)]

L= [(1,9), (2,8), (3,7), (4,6)]

occ= [[(0,0),(2,2)], [(0,1), (2,1)], [(0,2), (2,0)], [(1,0), (1,2)]]
chk= [False]*4

make= [[0]*3 for _ in range(3)]
make[1][1]=5


def test():
    s=0
    for i in range(3):
        s+=make[i][0]
    if s!=15:
        return False
    s=0
    for i in range(3):
        s+=make[i][2]
    if s!=15:
        return False
    s=0
    for i in range(3):
        s+=make[0][i]
    if s!=15:
        return False
    s=0
    for i in range(3):
        s+=make[2][i]
    if s!=15:
        return False
    
    return True

def cost():
    s=0
    for i in range(3):
        for j in range(3):
            s+= abs(make[i][j]-sq[i][j])
    return s

def backtrack(k):
    if all(chk):
        if test():
            return cost()
        else:
            return 1e9
    ans= 1e9
    for i in range(4):
        if not chk[i]:
            chk[i]=True
            tmp1, tmp2= 1e9, 1e9
            (a, b), (c,d)= occ[k]
            make[a][b]= L[i][0]
            make[c][d]= L[i][1]
            tmp1= backtrack(k+1)

            make[c][d]= L[i][0]
            make[a][b]= L[i][1]
            tmp2= backtrack(k+1)
            make[a][b]= 0
            make[c][d]= 0
            ans= min(ans, tmp1, tmp2)
            chk[i]=False
    return ans

print(backtrack(0))






