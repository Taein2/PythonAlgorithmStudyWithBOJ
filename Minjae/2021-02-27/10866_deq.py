from collections import deque
import sys; input= lambda:sys.stdin.readline().rstrip()
q=deque()
top=-1
for _ in range(int(input())):
    s= input()
    if s[1]=='u':
        top+=1
        num=int(s.split()[1])
        if s[5]=='b':
            q.append(num)
        else:
            q.appendleft(num)
    elif s[1]=='o':
        if top==-1:
            print(-1)
            continue
        if s[4]=='b':
            print(q[top])
            q.pop()
        else:
            print(q[0])
            q.popleft()
        top-=1
    elif s[1]=='i':
        print(top+1)
    elif s[1]=='m':
        if top==-1:
            print(1)
        else:
            print(0)
    elif s[1]=='r':
        if top==-1:
            print(-1)
            continue
        print(q[0])
    else:
        if top==-1:
            print(-1)
            continue
        print(q[top])
    
