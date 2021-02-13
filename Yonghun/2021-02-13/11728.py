A, B = map(int,input().split())

A_array = list(map(int,input().split()))
B_array = list(map(int,input().split()))

A_array.extend(B_array)
A_array.sort()

for i in A_array :
    print(i , end =" ")