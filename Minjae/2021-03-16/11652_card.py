n= int(input())
dic={}
for _ in range(n):
    el= int(input())
    if el in dic:
        dic[el]+=1
    else:
        dic[el]=1

mx=-1
ans=-1
for k in dic.keys():
    if dic[k]>mx:
        mx=dic[k]
        ans=k
    elif dic[k]==mx and k<ans:
            ans=k

print(ans)