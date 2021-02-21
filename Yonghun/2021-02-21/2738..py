n, m = map(int,input().split())

A_array = [list(map(int,input().split())) for _ in range(n)]
B_array = [list(map(int,input().split())) for _ in range(n)]

result = []

for p in range(n) :
    for q in range(m) :
        A_array[p][q] += B_array[p][q]

for i in A_array :
    for j in i :
        print(j, end = " ")
    print()