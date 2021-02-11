for _ in range(int(input())):
    q=[]
    s= input()
    q.append('(')
    if s[0]!='(':
        print('NO')
        continue

    flag=True
    for el in s[1:]:
        if el=='(':
            q.append('(')
        else:
            if not q:
                flag= False
                
                break
            q.pop()
    if flag and not q:
        print('YES')
    else:
        print('NO')