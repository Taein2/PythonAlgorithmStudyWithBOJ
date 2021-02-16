while True:
    s = input()
    if s == '*':
        break
    
    Flag = True
    for i in range(1, len(s)):
        word_list = []
        for j in range(len(s)-i):
            word = s[j] + s[j+i]
            word_list.append(word)
            
        if len(word_list) != len(set(word_list)):
            Flag = False
            break
            
    if Flag == True:
        print(f'{s} is surprising.')
    else:
        print(f'{s} is NOT surprising.')