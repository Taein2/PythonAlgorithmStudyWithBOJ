S = input()
T = input()
length = len(S)

def solve(text):
    if len(text) == length :
        if text == S :
            print(1)
            exit()
        return

    if text[0] == 'B':
        tmp = text[1:] 
        solve(tmp[::-1])
        
    if text[-1] == 'A':
        tmp = text[:-1]
        solve(tmp)

solve(T)
print(0)