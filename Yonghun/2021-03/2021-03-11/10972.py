def next_permutation(a):
    n = len(a) - 1
    i = n
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i == 0: # 마지막 순열
        return False
    j = n
    while a[i-1] >= a[j]: # 오른쪽에 있으면서 a[i-1]보다 큰 수
        j -= 1
    a[i-1], a[j] = a[j], a[i-1] # SWAP
    j = n
    while i < j:
        a[i], a[j] = a[j], a[i] # a[i]부터 순열 뒤집기
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))

if next_permutation(a) is True:
    for i in a:
        print(i, end=' ')
    print()
else:
    print(-1) # 마지막 순열