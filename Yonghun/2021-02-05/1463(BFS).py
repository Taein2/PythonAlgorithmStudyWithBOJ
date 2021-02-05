from collections import deque
import sys
input = sys.stdin.readline

n = int(input())


def bfs(x) :
    cnt = 0
    q = deque()
    q.append((x, cnt))
    while q :
        x, cnt = q.popleft()

        if x == 1 :
            return cnt
        if x % 2 == 0 :
            q.append((x // 2, cnt + 1))

        if x % 3 == 0 :
            q.append((x // 3 , cnt + 1))
        q.append((x - 1, cnt + 1))

    return -1
print(bfs(n))