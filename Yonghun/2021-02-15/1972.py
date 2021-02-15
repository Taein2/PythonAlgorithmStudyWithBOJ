while True:
    s = input()
    if s == '*':
        break
    
    result = True
    for i in range(1, len(s)):
        word_list = []
        for j in range(len(s)-i):
            word = s[j] + s[j+i]
            word_list.append(word)
        if len(word_list) != len(set(word_list)):
            result = False
            break
            
    if result == True:
        print("{} is surprising.".format(s))
    else:
        print("{} is NOT surprising.".format(s))