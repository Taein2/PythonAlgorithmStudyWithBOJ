form = input()
answer = 1

if form[0] == 'c' :
    answer = 26
else :
    answer = 10

for i in range(1, len(form)) :
    if form[i] == "c" :
        if form[i - 1] == 'c' :
            answer *= 25
        else :
            answer *= 26
    
    else :
        if form[i - 1] == 'd' :
            answer *= 9
        else :
            answer *= 10

    
print(answer)