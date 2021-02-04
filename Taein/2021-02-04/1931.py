import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
lst.sort(key = lambda x: (x[1],x[0]))
endTime = 0
count = 0
for i in range(N):
    if endTime <= lst[i][0]:
        endTime = lst[i][1]
        count+=1
print(count)