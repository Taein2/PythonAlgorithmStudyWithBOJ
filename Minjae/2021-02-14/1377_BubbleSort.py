n= int(input())
A= [0]+[int(input()) for _ in range(n)]

def bubblesort(A,n):
    change=False
    for i in range(1,n+2):
        change=False
        for j in range(1,n-i+1):
            if A[j]>A[j+1]:
                change=True
                A[j], A[j+1]= A[j+1], A[j]

        if change:
            print(i)
            break
bubblesort(A,n)