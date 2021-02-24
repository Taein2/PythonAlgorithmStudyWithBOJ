import sys
input = sys.stdin.readline
n,m = map(int,input().split())
# 5가 몇번 나누어지는지를 구한다.
def fiveCount(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

# 2가 몇번 나누어지는지를 구한다.
def twoCount(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer

if m == 0:
  print(0)
else:
  print(min(twoCount(n)-twoCount(m)-twoCount(n-m),fiveCount(n)-fiveCount(m)-fiveCount(n-m)))

'''
fact = fac(n)//(fac(m)*fac(n-m))
count = 0
while fact % 10 == 0:
  count += 1
  fact = fact // 10
print(count)
'''