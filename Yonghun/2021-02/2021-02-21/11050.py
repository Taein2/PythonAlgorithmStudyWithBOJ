# 이항 계수

n, k = map(int,input().split())

def fact(n, k) :
    if n == k :
        return 1
    elif k == 0 :
        return 1

    else :
        return fact(n-1, k-1) + fact(n-1,k)
    
print(fact(n,k))