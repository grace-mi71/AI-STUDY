n = int(input())
A = list(map(int, input().split()))

result=[]
x=0
for i in range(n):
    for j in range(n):
        x=x+A[j]*abs(j-i) #abs() 는 절댓값 함수
    result.append(x)
    x=0
print(min(result))
