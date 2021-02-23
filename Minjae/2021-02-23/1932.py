n= int(input())
mx=[0]*n
for j in range(1,n+1):
    line= [*map(int, input().split())]
    for i in range(len(line)-1,-1,-1):
        mx[i]=line[i]+max(mx[max(i-1,0)],mx[i])
print(max(mx))