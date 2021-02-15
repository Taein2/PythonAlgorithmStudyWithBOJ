while True:
    s= input()
    if s=='*':
        break
    last= len(s)-1
    
    if len(s)==1:
        print(f'{s} is surprising.')
        continue
    for i in range(1,last+1):
        flag=True
        dic={}
        for a, b in zip(s, s[i:]):
            if a+b in dic:
                flag=False
                break
            else:
                dic[a+b]=1
        if not flag:
            print(f'{s} is NOT surprising.')
            break
    if flag:
        print(f'{s} is surprising.')