import sys
input = sys.stdin.readline

def lotto(x,count):
    if count == 6:
        for i in range(k):
            if select[i]:
                print(S[i], end=' ')
        print()    
    for i in range(x,k):
        select[i] = 1
        lotto(i+1,count+1)
        select[i] = 0

while True:
    sk = list(map(int,input().split()))
    k = sk[0]
    if k == 0:
        break
    S = sk[1:]
    select = [0 for _ in range(k)]
    lotto(0, 0)
    print()