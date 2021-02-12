bloc= [0]*7
bloc[0]= [[0], [0,0,0,0]]
bloc[1]= [[0,0]]
bloc[2]= [[1, 1, 0], [0,1]]
bloc[3]= [[0, 1, 1], [1,0]]
bloc[4]= [[0, 0, 0], [1,0], [0,1], [0,1,0]]
bloc[5]= [[0, 0, 0], [0,2], [0,0], [1,0,0]]
bloc[6]= [[0, 0, 0], [0,0], [2,0], [0,0,1]]

c, p= map(int, input().split())
p-=1
h= [*map(int, input().split())]

def put(p):
    cnt=0
    for i in range(c):
        for blc in bloc[p]:
            if len(h[i:])<len(blc): continue
            fit=[]
            for floor, b in zip(h[i:], blc):
                fit.append(floor+b)
            isSame=True
            if len(fit)==1:
                cnt+=1
                continue
            isSame=True
            for a, b in zip(fit, fit[1:]):
                if a!=b:
                    isSame=False
                    break
            if isSame:
                cnt+=1
    return cnt
print(put(p))

            

