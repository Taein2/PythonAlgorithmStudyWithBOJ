a, b, c= map(int, input().split())

def mul(n,r):
    if r==1:
        return n%c
    chunk= mul(n,r//2)%c
    if r%2:
        return chunk*chunk*n%c
    else:
        return chunk*chunk%c
print(mul(a,b))