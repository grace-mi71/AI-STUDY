N = int(input())
arr = [int(input()) for _ in range(N)]
src=1
result=1

for i in range(1,N):
    if arr[i]*arr[i-1]>0:
        src+=1
        result=max(src,result)
    elif arr[i]*arr[i-1]<0:
        src=1

print(result)