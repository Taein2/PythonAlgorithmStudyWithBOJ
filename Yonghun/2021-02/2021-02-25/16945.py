# 매직 스퀘어
import sys
from itertools import permutations
input = sys.stdin.readline

def check(s):
    val = sum(s[0 : 3]) # 기준

    #가로 검사
    for i in range(0, 9, 3):
        if sum(s[i : i+3]) != val:
            return False

    #세로 검사
    for i in range(3):
        if val != s[i] + s[i+3] + s[i+6]:
            return False
    
    #대각선 검사
    sum_v = 0
    if s[0] + s[4] + s[8] != val:
        return False
    if s[2] + s[4]  +s[6] != val:
        return False

    return True

def calc(s):
    result = 0
    for i in range(3):
        for j in range(3):
            result += abs(array[i][j] - s[i*3 + j]) # 중요!
            # print(s[i*3 + j])
    return result

array = []
for _ in range(3):
    array.append(list(map(int,input().split())))

answer = int(10e9)

for i in permutations(range(1, 10), 9):
    if check(i):
        answer = min(answer, calc(i))
print(answer)