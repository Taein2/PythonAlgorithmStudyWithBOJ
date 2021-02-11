form= input()
flag=-1
ans=1
for el in form:
    if el=='d':
        if flag!=1:
            ans*=10
        else:
            ans*=9
        flag=1
    else:
        if flag!=0:
            ans*=26
        else:
            ans*=25
        flag=0
print(ans)


