n= int(input())
# ?
if n>0:
    mx=0
    i=-2
    while mx<n:
        i+=2
        mx=2**i
    print(i)
        



'''
1 4  16   64  256  1024
-2 -8 -32 -128  -512
'''