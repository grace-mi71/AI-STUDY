n, t = map(int, input().split())
arr = list(map(int, input().split()))
first_set=0
cnt=1
result=1

for i in range(n):
    if arr[i]>t:
        first_set+=1

if first_set>0:
    for j in range(1,n):
        if arr[j]>t and arr[j-1]>t:
            cnt+=1
            result=max(cnt, result)
        else: cnt=1
        
    print(result)

else: print(0)

# Please write your code here.