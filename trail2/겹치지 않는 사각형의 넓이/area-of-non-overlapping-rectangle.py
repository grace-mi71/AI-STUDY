x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

OFFSET=1000
for i in range(3):
    x1[i]+=OFFSET
    x2[i]+=OFFSET
    y1[i]+=OFFSET
    y2[i]+=OFFSET

n_list=[[0]*2000 for _ in range(2000)]

for x in range(2):
    for i in range(x1[x],x2[x]):
        for j in range(y1[x],y2[x]):
            n_list[i][j]=1

for a in range(x1[2],x2[2]):
    for b in range(y1[2],y2[2]):
        n_list[a][b]=0

result=sum(sum(row) for row in n_list)

print(result)