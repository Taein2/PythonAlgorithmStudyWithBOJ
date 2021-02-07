import sys
input = sys.stdin.readline
lst = []
arr = input().rstrip()
for i in range(len(arr)):
    lst.append(arr[i:])
lst.sort()
for i in range(len(arr)):
    print(lst[i])