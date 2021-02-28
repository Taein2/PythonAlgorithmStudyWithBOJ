n = int(input())
stack = []
answer = []

idx = 1
Flag = True
for i in range(n) :
    num = int(input())
    while idx <= num :
        stack.append(idx)
        answer.append('+')
        idx += 1
    if stack[-1] == num :
        stack.pop()
        answer.append('-')
    else :
        Flag = False

if Flag == False :
    print("NO")
else :
    for i in answer :
        print(i)