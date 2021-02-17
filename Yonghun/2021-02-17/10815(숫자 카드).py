def binary_search(array, target, start, end) :
    if start > end :
        return 0
    mid = (start + end) // 2

    if array[mid] == target :
        return 1
    
    elif array[mid] > target :
        return binary_search(array, target, start , mid - 1)
        
    else :
        return binary_search(array, target, mid + 1  ,end)

n = int(input())
n_array = list(map(int,input().split()))
n_array.sort()

m = int(input())
number = list(map(int,input().split()))

chk = [0] * m
result = []
start = 0
end = n - 1

for i in range(m) :
    result = binary_search(n_array, number[i], start, end)
    chk[i] = result

for i in chk :
    print(i , end =" ")

