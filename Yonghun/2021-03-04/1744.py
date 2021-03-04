# 수 묶기

# 양수,  양수 = 곱셈 
# 음수 , 음수 = 곱셈 
# 양수 , 음수 = 덧셈

# 0, 양수 = 덧셈, 
# 0, 음수 = 곱셈

# 1, 양수 = 덧셈 
# 1 ,음수 = 덧셈

n = int(input())
positive = []
negative = []
one = []

for _ in range(n) :
    num = int(input())

    if num > 1 :
        positive.append(num)
    
    elif num <= 0 :
        negative.append(num)
    
    else :
        one.append(num)

positive.sort(reverse = True) # 마지막에 + 하는 숫자가 제일 작아야한다.
negative.sort() # 만약 0이 있으면 오름차순으로 정렬했을 때 제일 끝에 있는 수가 0이므로 더했을 때 최댓값이 된다..?

result = 0

if len(positive) % 2 == 0 :
    for i in range(0, len(positive), 2) :
        result += positive[i] * positive[i + 1]
else :
    for i in range(0, len(positive) - 1, 2) :
        result += positive[i] * positive[i + 1]
    result += positive[-1] # 마지막 숫자 더하기


if len(negative) % 2 == 0 :
    for i in range(0, len(negative), 2) :
        result += negative[i] * negative[i + 1]
else :
    for i in range(0, len(negative) - 1, 2) :
        result += negative[i] * negative[i + 1]
    result += negative[-1] # 마지막 숫자 더하기

result += sum(one)

print(result)

