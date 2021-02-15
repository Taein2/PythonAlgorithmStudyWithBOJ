C, P = map(int,input().split())
heights = list(map(int,input().split())) # 맵의 높이 정보

# 블록의 바닥
B = [
    [[0], [0,0,0,0]], # 1
    [[0,0]], # 2 
    [[0,0,1], [1,0]], # 3
    [[1,0,0], [0,1]], # 4
    [[0,0,0], [0,1], [1,0], [1,0,1]], # 5
    [[0,0,0], [0,0], [2,0], [0,1,1]], # 6
    [[0,0,0], [0,0], [0,2], [1,1,0]] # 7
]

ans = 0

# c = 6 , p(블록 번호) = 5
for block in B[P - 1]: #  [0,0,0], [0,1], [1,0], [1,0,1]
    for i in range(0, C + 1 - len(block)):
        dif = heights[i] - block[0] 
        for j in range(len(block)): # 블록 전체가 높이가 맞는지 확인.
            if heights[i + j] - block[j] != dif :
                break
        else:
            ans += 1
print(ans)