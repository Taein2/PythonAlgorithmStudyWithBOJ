n, b= input().split()
b=int(b)
s= 0
for idx, el in enumerate(n[::-1]):
    if ord(el) in range(65,65+26):
        el= ord(el)-65+10
    el= int(el)
    s+=el*b**idx
print(s)