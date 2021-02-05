a= input().split('-')
b=[]
for el in a:
    tmp= el.split('+')
    chunk=0
    for num in tmp:
        chunk+=int(num)
    b.append(str(chunk))

print(eval('-'.join(b)))