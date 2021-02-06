from itertools import combinations as cb

while True :
    s = list(map(int,input().split()))
    if s[0] == 0 :
        break
    del s[0]
    s = list(cb(s,6))
    for i in s :
        for j in i :
            print(j, end =' ')
        print()
    print()