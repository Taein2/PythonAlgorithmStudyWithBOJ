import sys
input = sys.stdin.readline

a,b = map(int,input().split())
m = int(input())
lst = list(map(int,input().split()))
ten = 0
for i in range(m):
    ten += lst[-1] * (a**i)
    lst.pop()
result = []
while ten !=0 :
    result.append(ten % b)
    ten = ten // b
for i in range(len(result)-1,-1,-1):
    print(result[i],end=" ")
