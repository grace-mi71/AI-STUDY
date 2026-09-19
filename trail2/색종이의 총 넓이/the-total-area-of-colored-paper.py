n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
OFFSET=100
x, y = list(x), list(y)

for src in range(n):
    x[src]+=OFFSET
    y[src]+=OFFSET

n_list=[[0]*200 for _ in range(200)]

for cnt in range(n):
    for i in range(x[cnt], x[cnt]+8):
        for j in range(y[cnt], y[cnt]+8):
            n_list[i][j]=1

result=sum(sum(row) for row in n_list)

print(result)