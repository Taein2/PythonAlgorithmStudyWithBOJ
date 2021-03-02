import sys; input= lambda: sys.stdin.readline().rstrip()
q=[]
top=-1
for _ in range(int(input())):
    inp= input()
    if inp[1]=='u':
        num= int(inp.split()[1])
        q.append(num)
        top+=1
    elif inp[1]=='a':
        if top>=0:
            print(q[top])
        else:
            print(-1)
    elif inp[1]=='o':
        if top>=0:
            print(q[0])
            q.pop(0)
            top-=1
        else:
            print(-1)
    elif inp[1]=='i':
        print(top+1)
    elif inp[1]=='m':
        print([1,0][top>=0])
    elif inp[1]=='r':
        if top>=0:
            print(q[0])
        else:
            print(-1)