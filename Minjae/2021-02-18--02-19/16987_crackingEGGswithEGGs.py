n= int(input())
B= []
for _ in range(n):
    a, b=map(int, input().split())
    B.append([a,b])

mx=-1

def backtrack(idx, cnt):
    global mx
    if idx==n:
        return
    thr_dur, thr_wei = B[idx]
    if thr_dur==0:
        backtrack(idx+1, cnt)
        return # 이거 안해줬었음 ㅜㅜ
    #backtrack(idx+1, cnt) # 안고르고 가는것도 있어여?
    for i in range(n):
        if i==idx or not B[i][0]:
            continue
        print(B)
        print(idx,'->',i)
        def_dur, def_wei= B[i]
        ori=[def_dur, thr_dur, cnt]
        if thr_wei >= def_dur:
            cnt+=1
            B[i][0]=0
        else: 
            def_dur-=thr_wei
            B[i][0]= def_dur
        if thr_dur<=def_wei:
            B[idx][0]=0
            cnt+=1
        else:
            thr_dur-=def_wei
            B[idx][0]=thr_dur

        print(B,cnt)
        if i==n-1:
            mx=max(mx,cnt)
        backtrack(idx+1, cnt)
        B[i][0]= ori[0]
        B[idx][0]=ori[1]
        cnt=ori[2]
        

backtrack(0, 0)
print(mx)

'''
3
213 295
153 24
15 233
'''