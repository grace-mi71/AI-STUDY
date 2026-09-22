n = int(input())
arr = [int(input()) for _ in range(n)]
src=1
arr_score=1
for i in range(n):
    if i==0:
        src=1
    elif i!=0 and arr[i]!=arr[i-1]:
        arr_score=max(src, arr_score)
        src=1
    elif i!=0 and arr[i]==arr[i-1]:
        src+=1
        arr_score=max(src,arr_score)

print(arr_score)