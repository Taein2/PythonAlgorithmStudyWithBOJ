# 단어 수학

n = int(input())

# n개의 단어
word = []
for _ in range(n) :
    w = input()
    word.append(list(w))

charDic = {}

#문자의 자릿수에 따라 10의 n승 더해주기
# ex) G:100, C:10, F:1
for i in range(len(word)) :
    for j in range(len(word[i])) :
        if word[i][j] not in charDic :
            charDic[word[i][j]] = pow(10, len(word[i]) - j - 1)
        else :
            charDic[word[i][j]] += pow(10, len(word[i]) - j - 1)


# value 값을 기준으로 내림차순 정렬
sort_list = sorted(charDic.items(), key=lambda x: x[1], reverse=True)
print(sort_list)


result, num = 0, 9

#정렬된 값이 앞에 있을수록 자릿수가 크다는 거니까 9부터 곱해주면서 결과에 더해주기
for i in range(len(sort_list)):
    result += num * sort_list[i][1]
    num -= 1

print(result)

#https://hazung.tistory.com/126