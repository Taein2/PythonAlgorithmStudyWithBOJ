a, b=input().split()
b=int(b)
L= sorted(map(int, list(a)),reverse=True)

ans=-1
def f(s, num):
    if not num:
        if s<b:
            print(s)
            exit()
        return
    leng=len(num)
    for i in range(leng):
        if not num[i]:
            continue
        tmp=num[:]
        tmp.pop(i)
        f(s*10+num[i],tmp)


f(0, L)
print(-1)