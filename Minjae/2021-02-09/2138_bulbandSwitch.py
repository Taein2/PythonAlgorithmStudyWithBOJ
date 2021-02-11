n= int(input())
mid= (n-1)//2
# lefe
a= [int(i) for i in input()]
b= [int(i) for i in input()]
L=[0]*n
M=[0]*n

for idx, (x, y) in enumerate(zip(a,b)):
    if x!=y:
        L[idx]=1
'''
왼쪽부터 차레대로만 스위치를 누를 수 있다면,
더이상 건드릴 수 없는 전구: 마지막으로 답으로 바꿔야하는 전구가 있을것.
근데 1번 스위치는 눌러소 더이상 못건드는 전구를 만들 수 없는데, 
1번스위치를 눌러서 2번전구를 같이 바꿔놔야 되는 경우가 있다
'''
M= L[:]
switch=0 
for i in range(1, n):
    if L[i-1]: 
        L[i-1]^=1
        switch+=1
        L[i]^=1
        if i+1<n:
            L[i+1]^=1
if 1 in L:
    switch=1
    M[0]^=1
    M[1]^=1
    for i in range(1, n):
        if M[i-1]:
            M[i-1]^=1
            switch+=1
            M[i]^=1
            if i+1<n:
                M[i+1]^=1
if 1 not in L or 1 not in M:
    print(switch)
else:
    print(-1)