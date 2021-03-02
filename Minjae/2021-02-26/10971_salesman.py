
import sys
input = sys.stdin.readline
# print = sys.stdout.write

def find(node, visited):
    print(node, bin(visited)[2:])
    if dp[node][visited] != 0:
        return dp[node][visited]
    
    if visited == (1 << N) -1:
        return graph[node][start_node] or sys.maxsize
    
    cost = sys.maxsize
    for idx, el in enumerate(graph[node]):
        print(f'({visited} >> {idx}) % 2 = {(visited >> idx) % 2}')
        if (visited >> idx) % 2 == 0 and el != 0:
            tmp = find(idx, visited | (1<<idx))
            cost = min(cost, tmp + el)
    dp[node][visited] = cost
    [print(*el) for el in dp]
    print()
    return cost

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
start_node = 0

print(find(start_node, 1))
