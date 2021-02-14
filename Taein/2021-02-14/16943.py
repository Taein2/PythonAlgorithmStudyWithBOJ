import sys
input = sys.stdin.readline

def solve(idx, num):
    global answer
    if idx == length:
        if int(num) <= int(''.join(map(str,b))):
            answer = max(answer, int(num))
        return
    for i in range(length):
        if idx == 0 and a[i] == 0:
            continue
        if not check[i]:
            check[i] = True
            solve(idx+1, num + str(a[i]))
            check[i] = False
    
a,b = input().split()
a = list(map(int, a.rstrip()))
b = list(map(int, b.rstrip()))
answer = -1
length = len(a)
check = [False]*length
solve(0,'')
print(answer)