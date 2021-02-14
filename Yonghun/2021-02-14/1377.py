import sys 
input = sys.stdin.readline
N = int(input()) 
nums = [] 
for i in range(N): 
    num = int(input())
    nums.append((num, i)) 
    
sorted_nums = sorted(nums) 

answer = 0 
for i in range(N): 
    answer = max(sorted_nums[i][1] - i + 1, answer) 
    
print(answer)

