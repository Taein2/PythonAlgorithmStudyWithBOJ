import sys
input = sys.stdin.readline
from math import factorial as fac
n,m = map(int,input().split())
fact = str(fac(n)//(fac(m)*fac(n-m)))
count = 0
flag = True
for i in range(len(fact)-1,-1,-1):
  if int(fact[i]) == 0:
    if flag:
      count += 1
  else:
    flag = False
    break
print(count)
