n = int(input())
x1, y1, x2, y2 = [], [], [], []
OFFSET=100
result=0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a+OFFSET)
    y1.append(b+OFFSET)
    x2.append(c+OFFSET)
    y2.append(d+OFFSET)

n_list=[[0]*200 for _ in range(200)]


for cnt in range(n):
    for i in range(x1[cnt], x2[cnt]):
        for j in range(y1[cnt], y2[cnt]):
            n_list[i][j]=1

result=sum(sum(row) for row in n_list)
print(result)
