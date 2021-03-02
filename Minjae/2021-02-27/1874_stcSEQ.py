n= int(input())
L= [int(input()) for _ in range(n)]
q=[]
cur=1
top=-1
ans=[]
for el in L:
    if top<0:
        q.append(cur)        
        top+=1
        cur+=1
        ans.append('+')
    while q[top]<el:
        q.append(cur)
        top+=1
        ans.append('+')
        cur+=1
    if q[top]==el:
        q.pop()
        top-=1
        ans.append('-')
        continue
    if q[top]>el:
        print('NO')
        exit()
    
print('\n'.join(ans))