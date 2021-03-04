# TLE
n= int(input())

def f(num, step, buffer,jumped):
    #print(num,step,buffer,jumped)
    global n
    if step+1==n:
        return max(num+1,num+buffer)
    if step==n:
        return num
    if step>n:
        return -1
    tmp=-1
    if not jumped:
        tmp=max(tmp,f(num,step+2,num,True))# 점프하거나
    if buffer: 
        tmp= max(tmp,f(num+buffer,step+1,buffer,False)) # push

    tmp= max(tmp, f(num+1,step+1,buffer,False)) # +1

    return tmp



print(f(1,1,0,False))

# n^2, 2n 속도 조절해보기