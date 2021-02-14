import sys
import itertools
input = sys.stdin.readline

n = int(input())
matrix = []
for i in range(n) :
    matrix.append(list(map(int, input().strip().split())))


gab = 1e9

team = [i for i in range(n)]

tt = list(itertools.combinations(team, n // 2))
for team1 in tt :
    team2 = [x for x in team if x not in team1]
    team1_score = 0
    team2_score = 0

    for x, y in list(itertools.combinations(team1, 2)) :
        team1_score += matrix[x][y] + matrix[y][x]

    for x, y in list(itertools.combinations(team2, 2)) :
        team2_score += matrix[x][y] + matrix[y][x]

    gab = min(gab,abs(team1_score-team2_score))



print(gab)