import sys
from itertools import combinations as cb
input = sys.stdin.readline
gab = 1e9

n = int(input())
matrix = []
for i in range(n) :
    matrix.append(list(map(int,input().split())))


team = [i for i in range(n)]
tt = list(cb(team, n // 2))

for team1 in tt :

    team2 = []
    for t in team :
        if t not in team1 :
            team2.append(t)

    # team2 = [x for x in team if x not in team1]
    team1_score = 0
    team2_score = 0

    for x, y in list(cb(team1, 2)) :
        team1_score += matrix[x][y] + matrix[y][x]

    for x, y in list(cb(team2, 2)) :
        team2_score += matrix[x][y] + matrix[y][x]

    gab = min(gab,abs(team1_score - team2_score))



print(gab)
