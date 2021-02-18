import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
check = list(map(int,input().split()))
for i in check:
    left , right = 0, n-1
    flag = False
    while left <= right:
        mid = (left + right) //2 
        if card[mid] == i:
            flag = True
            break
        elif card[mid] < i:
            left = mid + 1
        else:
            right = mid - 1
    print(1,end=" ") if flag else print(0,end=" ")
