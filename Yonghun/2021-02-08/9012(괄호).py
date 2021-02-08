T = int(input())

def check(bracket) :
    stack = []
    for i in bracket :
        if i == "(" :
            stack.append(i)
        if i == ")" :
            if len(stack) == 0 :
                stack.append(i)
            if stack[-1] == "(" :
                stack.pop()
            
    if len(stack) :
        return False
    else :
        return True


for _ in range(T) :
    bracket = list(input())
    answer = check(bracket)
    if answer :
        print('YES')
    else :
        print("NO")
    

