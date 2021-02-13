n, m= map(int, input().split())
a= [*map(int, input().split())]
b= [*map(int, input().split())]

i= 0
j= 0
while i<n or j<m:
    #print(f'({i} {j})')
    if i<n and j<m:
        if a[i]<b[j]:
            print(a[i], end=' ')
            i+=1
        else:
            print(b[j], end=' ')
            j+=1
    elif i==n:
        print(b[j], end=' ')
        j+=1
    else:
        print(a[i], end=' ')
        i+=1

