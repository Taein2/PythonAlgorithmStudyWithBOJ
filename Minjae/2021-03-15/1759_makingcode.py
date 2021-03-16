import sys; input= lambda: sys.stdin.readline().rstrip()
l, c= map(int, input().split())

ls=[]
for el in input().split():
    ls.append(ord(el))
ls.sort()

vs=[]
for el in ('a','e','i','o','u'):
    vs.append(ord(el))


def backtrack(i,n,s,voweled,changed,cnst):
    global c

    if n==l and voweled and changed and cnst>=2:
        print(s)
    if i==c:
        return
    if ls[i] in vs:
        backtrack(i+1,n+1,s+chr(ls[i]),True,True,cnst)
    else:
        backtrack(i+1,n+1,s+chr(ls[i]),voweled,True,cnst+1)
    backtrack(i+1, n, s, voweled,False,cnst)

backtrack(0,0,'',False,False,0)