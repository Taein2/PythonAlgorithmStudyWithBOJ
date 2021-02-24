board=[]
board.append([-1]*7)
board+= [[-1]+list(input().split())+[-1] for _ in range(5)]
board.append([-1]*7)

dx=[0,0,-1,1]
dy=[1,-1,0,0]

dic={}
def jump(i, j, k, num):
    if board[i][j]==-1:
        return
    num+=board[i][j]
    if k==5:
        if num not in dic:
            dic[num]=1
        return
    for y, x in zip(dy, dx):
        jump(i+y,j+x,k+1,num)

for i in range(1,1+5):
    for j in range(1,1+5):
        jump(i,j,0,'')

print(len(dic.keys()))