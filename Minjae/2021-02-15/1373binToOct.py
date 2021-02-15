a= input()
#num= int(a,2)
#print(oct(num)[2:])
n= len(a)
ans=[]
for i in range(n, -1, -3):
    sum=0
    for idx, b in enumerate(a[max(i-3,0):i][::-1]):
        sum+=int(b)*2**(idx)
    ans.append(str(sum))
    
print(int(''.join(ans[::-1])))