n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)
OFFSET=100
n_list=[[0]*200 for _ in range(200)]

for i in range(n):
    x1[i]+=OFFSET
    x2[i]+=OFFSET
    y1[i]+=OFFSET
    y2[i]+=OFFSET

for cnt in range(n):
    if cnt%2==1:
        for i in range(y1[cnt], y2[cnt]):
            for j in range(x1[cnt], x2[cnt]):
                n_list[i][j]=1
    else:
        for i in range(y1[cnt], y2[cnt]):
            for j in range(x1[cnt], x2[cnt]):
                n_list[i][j]=0

result=sum(sum(row) for row in n_list)

print(result)        