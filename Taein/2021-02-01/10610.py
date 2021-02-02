
import sys
input = sys.stdin.readline().rstrip

N = list(input())

result = 0
if '0' in N:
    N.sort(reverse=True)
    for i in range(len(N)):
       result += int(N[i])
    if result % 3 == 0:
        print(''.join(N))
    else:
        print(-1)
else :
   print(-1)
   
