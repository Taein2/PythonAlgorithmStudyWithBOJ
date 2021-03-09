negative = [-5]
result = 0
for i in range(0, len(negative) - 1, 2) :
        result += negative[i] * negative[i + 1]
result += negative[-1] # 마지막 숫자 더하기

print(result)