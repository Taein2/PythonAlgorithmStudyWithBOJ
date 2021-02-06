e, s, m= [int(i)-1 for i in input().split()]
for i in range(27000):
    if i%15==e and i%28==s and i%19==m:
        print(i+1)
        break