n= int(input())

st= str(n)
ans=0
ans+=n
for i in range(1,len(st)):
    ans=ans+n-10**i+1
print(ans)