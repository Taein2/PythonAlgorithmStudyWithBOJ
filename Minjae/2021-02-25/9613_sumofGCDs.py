for _ in range(int(input())):
    n, *L,=[*map(int, input().split())]


    def gcd(a, b):
        if not a*b:
            return a+b
        if a>b:
            return gcd(a%b, b)
        else:
            return gcd(a,b%a)

    chk= [False]*n
    def backtrack(i,q):
        if len(q)>=2:
            return gcd(q[0], q[1])
        if i==n:
            return 0

        sum=0
        for j in range(i,n):
            if not chk[j]:
                chk[j]=True
                q.append(L[j])
                sum+=backtrack(j+1,q)
                q.pop()
                chk[j]=False


        return sum
    print(backtrack(0,[]))

