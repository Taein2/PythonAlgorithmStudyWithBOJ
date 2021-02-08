n, s= map(int, input().split())
L= [*map(int, input().split())]

cnt=0
def backtrack(i,sm):
    global cnt
    if i>=n:
        return
    if sm+L[i]==s:
        cnt+=1
    backtrack(i+1, sm+L[i])
    backtrack(i+1, sm)
    

backtrack(0, 0)
print(cnt)