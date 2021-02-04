import sys; input= lambda: sys.stdin.readline().rstrip(); r=range
h, w= map(int, input().split())
n= int(input())
stic= []
for _ in r(n):
    a, b= map(int,input().split())
    stic.append((a, b))

ans= 0
for i in r(n-1):
    for j in r(i+1, n):
        ah, aw= stic[i]
        bh, bw= stic[j]
        
        if max(ah,bh)<=h and aw+bw<= w:
            ans= max(ans, ah*aw+ bh*bw)
        if ah+bh<=h and max(aw,bw)<=w:
            ans= max(ans, ah*aw+ bh*bw)

        bh, bw= bw, bh
        if max(ah,bh)<=h and aw+bw<= w:
            ans= max(ans, ah*aw+ bh*bw)
        if ah+bh<=h and max(aw,bw)<=w:
            ans= max(ans, ah*aw+ bh*bw)

        ah, aw= aw, ah
        if max(ah,bh)<=h and aw+bw<= w:
            ans= max(ans, ah*aw+ bh*bw)
        if ah+bh<=h and max(aw,bw)<=w:
            ans= max(ans, ah*aw+ bh*bw)

        bh, bw= bw, bh
        if max(ah,bh)<=h and aw+bw<= w:
            ans= max(ans, ah*aw+ bh*bw)
        if ah+bh<=h and max(aw,bw)<=w:
            ans= max(ans, ah*aw+ bh*bw)
print(ans)
