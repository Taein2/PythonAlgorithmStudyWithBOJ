n, c= map(int, input().split())

L= [int(input()) for _ in range(n)]
L.sort()

def install(k):
    global n,c
    stock=c-1
    wire=k
    cur=L[0]
    for idx,el in enumerate(L[1:]): 
        if el-cur<k:# 가까우면 설치못함
            continue
        else:
            stock-=1
            cur=el

    if stock>0:
        return False
    return True

def BS():
    lo=0
    hi=int(1e9)

    while lo+1<hi:
        m= (lo+hi)//2
        if install(m): # 설치할수있으면 늘려보기
            lo=m
        else:
            hi=m-1
    if install(hi):
        return hi
    else:
        return lo

print(BS())

'''
1 2 4 8 9
'''