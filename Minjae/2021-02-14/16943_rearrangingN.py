a, b=input().split()
b=int(b)
L= sorted(map(int, list(a)),reverse=True)

ans=-1
def f(s, num):
    if not num:
        if len(str(s))<len(a):
            return
        if s<b:
            print(s)
            exit()
        return
    leng=len(num)
    for i in range(leng):
        tmp=num[:]
        tmp.pop(i)
        f(s*10+num[i],tmp)


f(0, L)
print(-1)