import sys

input = sys.stdin.readline

N = int(input())
lst = [0,1,1]

for i in range(3,N+1):
    lst.append(lst[i-1]+lst[i-2])
print(lst[-1])