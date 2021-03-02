n= int(input())
A= [0]+[int(input()) for _ in range(n)]+[0]

def bubblesort(A,n):
    change=False
    for i in range(1,n+2):
        change=False
        for j in range(1,n-i+1):
            if A[j]>A[j+1]:
                change=True
                A[j], A[j+1]= A[j+1], A[j]
        print(A)
        if not change:
            print(i)
            break
bubblesort(A,n)

'''
2 3 9 4
9 3 4 2

2 3 4 9
'''