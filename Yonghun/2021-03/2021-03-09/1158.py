from collections import deque
n, k = map(int,input().split())

array = [i for i in range(1, n + 1)]
josephus = deque(array)

answer = []
while len(josephus) > 0 :
    for i in range(k) :
        tmp = josephus.popleft()
        josephus.append(tmp)
    answer.append(josephus.pop())


print("<" ,end = "")
for i in answer :
    if i == answer[-1] :
        print(i, end= "")
    else :
        print("%s, " %(i), end='')

print(">")