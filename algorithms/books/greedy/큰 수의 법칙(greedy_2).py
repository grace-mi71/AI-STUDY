import sys
# input=sys.stdin.readline().rstrip()
n,m,k=map(int, input().split())
data=list(map(int,input().split()))

data.sort(reverse=True)
first_size=data[0]
second_size=data[1]
result=0

while True:
    for i in range(k):
        if m==0:
            break
        result+=first_size
        m-=1
    if m==0:
        break
    result+=second_size
    m-=1

print(result)
