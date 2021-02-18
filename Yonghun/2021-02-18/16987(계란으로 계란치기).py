N = int(input()) # 계란의 수
duration = [] # 계란의 내구도
Weight = [] # 무게

for i in range(N):
    a, b = list(map(int, input().split()))
    duration.append(a)
    Weight.append(b)

# 정답
answer = 0

# n번째 계란으로 깨기
def dfs(n):
    global answer

    if n >= N :
        cnt = 0
        for life in duration:
            if life <= 0:
                cnt += 1

        answer = max(cnt, answer)
        return

    # 깨진 계란으로 때리는 경우
    if duration[n] <= 0:
        dfs(n + 1) # 다음 계란으로 다시 시작.
    
    else:
        Flag = False # 내려쳤는지 안쳤는지 판단.
        for i in range(N):
            if n == i or duration[i] <= 0 : 
                continue

            duration[n] -= Weight[i]
            duration[i] -= Weight[n]

            dfs(n + 1)

            duration[n] += Weight[i]
            duration[i] += Weight[n]

        # 더 이상 칠 수 있는 계란이 없다면
        if Flag == False :
            dfs(N)

dfs(0)
print(answer)