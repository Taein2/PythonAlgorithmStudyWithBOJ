n, r, c= map(int, input().split())

def rec(i, j, Len,accu):
    global r, c
    if i==r and j==c:
        return accu

    half= Len//2
    area=half*half

    if r<i+half:
        if c<j+half:
            return rec(i,j,half,accu)
        else:
            return rec(i,j+half,half,accu+area)
    else:
        if c<j+half:
            return rec(i+half,j,half,accu+2*area)
        else:
            return rec(i+half,j+half,half,accu+3*area)

print(rec(0, 0, 2**n, 0))