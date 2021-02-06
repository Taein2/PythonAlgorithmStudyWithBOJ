import sys; input= lambda: sys.stdin.readline().rstrip(); r= range
while True:
    L= [*map(int, input().split())]
    if not L[0]: break
    L[0]+=1
    for a in r(1,L[0]-5):
        for b in r(a+1,L[0]-4):
            for c in r(b+1,L[0]-3):
                for d in r(c+1,L[0]-2):
                    for e in r(d+1,L[0]-1):
                        for f in r(e+1,L[0]):
                            print(L[a], L[b], L[c], L[d], L[e], L[f]) 
    print()