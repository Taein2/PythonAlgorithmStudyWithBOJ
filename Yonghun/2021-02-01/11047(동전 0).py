import sys
input = sys.stdin.readline
n, k = map(int,input().split())

coin_list = []
for i in range(n) :
    coin = int(input())
    coin_list.append(coin)


coin_list.sort(reverse = True)
count = 0 

while 1 :
    if k == 0 :
        break

    for coin in coin_list :
        if coin > k :
            continue

        if k >= coin :
            k -= coin
            count += 1
            break

print(count)