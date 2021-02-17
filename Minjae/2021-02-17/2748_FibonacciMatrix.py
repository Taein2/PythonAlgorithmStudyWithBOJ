import sys; sys.setrecursionlimit(100000)
n=int(input())
dp= [[[1,1],[1,0]]]+ [[[1,1],[1,0]]]+[[[0,0],[0,0]] for _ in range(n)]

def fibo(n):
    if n<=1:
        if n==-1:
            return [[0,0],[0,0]]
        return dp[n]
    if dp[n]==[[0,0],[0,0]]:
        x=fibo(n//2)
        a= x[0][0]
        b= x[0][1]
        c= x[1][0]
        d= x[1][1]
        if n%2:
            dp[n]= [[a**2+b*c+b*(a+d), a**2+b*c], [c*(a+d)+ b*c+d**2, b*(a+d)]]
        else:
            dp[n]= [[a**2+b*c, b*(a+d)], [c*(a+d), b*c+d**2]]
        return dp[n]
    else:
        return dp[n]

print(fibo(n-1)[0][0])

