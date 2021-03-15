from itertools import combinations

L, C = map(int,input().split())
array = list(map(str,input().split()))
array.sort()


vowels = ['a','e','i','o','u']

comb = list(combinations(array,L))

for word in comb :
    count_vowel = 0 # 모음의 개수
    count_consonant = 0 # 자음의 개수
    for letter in word :
        if letter in vowels :
            count_vowel += 1
        else :
            count_consonant += 1

    
    if 1 <= count_vowel and 2 <= count_consonant :
        print("".join(word))
    
