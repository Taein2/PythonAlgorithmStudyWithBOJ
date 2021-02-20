a= input()
b= input()

def rec(b):
    if b==a:
        return True
    if len(a)>=len(b):
        return False
    if b[-1]=='A' and rec(b[:-1]):
        return True
    return b[-1]=='B' and rec(b[:-1][::-1]) 
if rec(b):
    print(1)
else:
    print(0)