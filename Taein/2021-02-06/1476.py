import sys
input = sys.stdin.readline
E,S,M = map(int,input().split())

year = 1
while not ((year-E) % 15 == 0 and (year-S) % 28 == 0 and (year-M) % 19 == 0):
    year += 1
print(year)

