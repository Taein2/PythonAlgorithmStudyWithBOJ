import sys

input = sys.stdin.readline

N = int(input())
RGB = [list(map(int,input().split())) for _ in range(N)]

for i in range(N-1):
    RGB[i+1][0] += min(RGB[i][1],RGB[i][2]) #빨강
    RGB[i+1][1] += min(RGB[i][0],RGB[i][2]) #초록
    RGB[i+1][2] += min(RGB[i][0],RGB[i][1]) #파랑
print(min(RGB[N-1]))
