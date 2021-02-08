n = int(input())
opr = input().split()
check = [False] * 10
max_num = ""
min_num = ""

# 부등호 조건이 만족할 때만 작동
def possible(i, j, k): 
    if k == ">":
        return i > j
    else:
        return i < j


def dfs(cnt, s):
    global max_num, min_num
    if cnt > n : #맨 처음 나타나는 값이 최소, 마지막 저장되는 것이 최대
        if len(min_num) == 0:
            min_num = s
        else:
            max_num = s
        return
    for i in range(10) : 
        if check[i] == False:
            if cnt == 0 or possible(s[-1], str(i), opr[cnt - 1]):
                check[i] = True
                dfs(cnt + 1, s + str(i))
                check[i] = False

dfs(0, "")
print(max_num)
print(min_num)