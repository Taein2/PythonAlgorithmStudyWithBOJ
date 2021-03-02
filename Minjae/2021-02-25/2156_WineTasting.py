n= int(input())
L= [int(input()) for _ in range(n)]

a, b, c= 0, L[0], 0 # 이번꺼 안마심, 이번껄 첫자능로 마심, 이번껄 둘째잔으로 마심
prva=0
for i in range(1,n):
    a, b, c, prva= max(b,c), max(a+L[i], prva+L[i]), b+L[i],a

print(max(a,b,c))