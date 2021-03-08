from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = []
cctvs = [] # cctv의 위치와 번호(종류)를 담은 리스트

for x in range(n) :
    temp = list(map(int,input().split()))
    for y in range(m) :
        if 1 <= temp[y] <= 5 :
            cctvs.append([x,y,temp[y]]) # cctv이면 cctvs에 현재 위치와 cctv의 번호(종류) 추가

    maps.append(deepcopy(temp))

answer = 1e9

#----------------------------------------------------------------

# dirs : cctv가 감시할 수 있는 방향
# 0 = 왼쪽
# 1 = 위
# 2 = 오른쪽
# 3 = 아래

def check_map(array, dirs, x, y) : # maps에 # 표시하는 함수
    array = deepcopy(array)
    for looking in dirs :
        if looking == 0 : # 왼쪽, x 고정
            for dy in range(y, -1, -1) :
                if array[x][dy] == 6 :
                    break
                elif array[x][dy] != 0 :
                    continue
                else :
                    array[x][dy] = '#'
        elif looking == 1 : # 위쪽, y 고정
            for dx in range(x, -1, -1) :
                if array[dx][y] == 6 :
                    break
                elif array[dx][y] != 0 :
                    continue
                else :
                    array[dx][y] = '#'
        elif looking == 2 : # 오른쪽, x 고정
            for dy in range(y, len(array[0])) :
                if array[x][dy] == 6 :
                    break
                elif array[x][dy] != 0 :
                    continue
                else :
                    array[x][dy] = '#'
        elif looking == 3 : # 아래쪽, y 고정
            for dx in range(x, len(array)) :
                if array[dx][y] == 6 :
                    break
                elif array[dx][y] != 0 :
                    continue
                else :
                    array[dx][y] = '#'  

    return array


def detecting(array, cctvs, idx) :
    global answer

    if idx == len(cctvs) :
        cnt = 0
        for x in range(len(array)) :
            cnt += array[x].count(0)
        
        answer = min(answer, cnt)
        return
    
    cctv = cctvs[idx]
    x, y, kind = cctv

    if kind == 1 :
        for i in range(4) :
            next_array = check_map(array, [i], x, y)
            detecting(next_array, cctvs, idx + 1)

    if kind == 2 :
        for i in [(0,2), (1,3)] :
            next_array = check_map(array, i, x ,y)
            detecting(next_array, cctvs, idx + 1)

    if kind == 3 :
        for i in [(1,2),(2,3),(3,0),(0,1)] :
            next_array = check_map(array, i, x, y) 
            detecting(next_array, cctvs , idx + 1)
    
    if kind == 4 :
        for i in [(0,1,2),(1,2,3),(2,3,0),(3,0,1)] :
            next_array = check_map(array, i, x, y)
            detecting(next_array, cctvs, idx + 1)

    if kind == 5 : 
        next_array = check_map(array, (0,1,2,3), x, y)
        detecting(next_array, cctvs, idx + 1)


detecting(maps, cctvs , 0)
print(answer)