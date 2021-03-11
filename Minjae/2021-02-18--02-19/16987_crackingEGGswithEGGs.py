n= int(input())
B= []
for _ in range(n):
    a, b=map(int, input().split())
    B.append([a,b])

mx=-1

def backtrack(idx, cnt):
    global mx
    mx=max(mx,cnt)
    if idx==n:
        return
    thr_dur, thr_wei = B[idx]
    if thr_dur==0:
        backtrack(idx+1, cnt)
        return # 이거 안해줬었음 ㅜㅜ
    for i in range(n):
        if i==idx or not B[i][0]:
            continue
        def_dur, def_wei= B[i]
        cracked=0
        if thr_wei >= def_dur:
            cracked+=1
            B[i][0]=0
        else: 
            B[i][0]= def_dur-thr_wei
        if thr_dur<=def_wei:
            B[idx][0]=0
            cracked+=1
        else:
            B[idx][0]=thr_dur-def_wei

        backtrack(idx+1, cnt+cracked)
        B[i][0]= def_dur
        B[idx][0]= thr_dur
        

backtrack(0, 0)
print(mx)

'''
3
213 295
153 24
15 233
'''