import sys
input = sys.stdin.readline

n = int(input())
state = list(map(int,input().rstrip()))
result = list(map(int,input().rstrip()))

def zeroClick(state):
    count=1
    state[0]=int(not state[0])
    state[1] = int(not state[1])
    for i in range(1,n):
        if(state[i-1]!=result[i-1]):
            count+=1
            state[i-1]=int(not state[i-1])
            state[i]=int(not state[i])
            if(i!=n-1):
                state[i+1]=int(not state[i+1])
    if(state==result):
        return count
    else:
        return -1
def zeroNoClick(state):
    count=0
    for i in range(1,n):
        if(state[i-1]!=result[i-1]):
            count+=1
            state[i-1]=int(not state[i-1])
            state[i]=int(not state[i])
            if(i!=n-1):
                state[i+1]=int(not state[i+1])
    if(state==result):
        return count
    else:
        return -1

res1 = zeroClick(state[:])
res2 = zeroNoClick(state[:])
if(res1>=0 and res2>=0):
    print(min(res1,res2))
elif(res1>=0 and res2<0):
    print(res1)
elif(res1<0 and res2>=0):
    print(res2)
else:
    print(-1)