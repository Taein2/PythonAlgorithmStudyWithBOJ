import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [input() for _ in range(n)]
check = [[False]*m for _ in range(n)]   # 십자가를 만드는 데 * 사용되는 지 채크
ans = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            l = 0    # 십자가 길이 저장 공간
            k = 1    # 십자가 길이
            while True:
                if i+k < n and i-k >= 0 and j+k < m and j-k >= 0:
                    if a[i+k][j] == '*' and a[i-k][j] == '*' and a[i][j+k] == '*' and a[i][j-k] == '*':
                        l = k   # 십자가 길이 저장
                    else:
                        break
                else:
                    break
                k += 1    # 한 단계 더 큰 십자가 확인을 위해 k + 1
            if l > 0:   # 십자가가 있다면
                ans.append((i+1,j+1,l))   # ans에 좌표, 크기 추가
                check[i][j] = True        # 사용된 * 위치에 해당하는 check 값 변경
                for k in range(1, l+1):
                    check[i+k][j] = True
                    check[i-k][j] = True
                    check[i][j+k] = True
                    check[i][j-k] = True

for i in range(n):       # 사용되지 않은 * 있는 지 확인
    for j in range(m):
        if a[i][j] == '*' and check[i][j] == False:
            print(-1)
            exit()
print(len(ans))  # 십자가 수 출력
for p in ans:    # 위치, 크기 출력
    print(' '.join(map(str,p)))