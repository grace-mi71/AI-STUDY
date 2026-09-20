x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
OFFSET=1000
for x in range(2):
    x1[x]+=OFFSET
    x2[x]+=OFFSET
    y1[x]+=OFFSET
    y2[x]+=OFFSET

n_list=[[0]*2000 for _ in range(2000)]
x_list=[]
y_list=[]

for i in range(y1[0], y2[0]):
    for j in range(x1[0], x2[0]):
        n_list[i][j]=1

for a in range(y1[1], y2[1]):
    for b in range(x1[1], x2[1]):
        n_list[a][b]=0

for cnt1 in range(2000):
    for cnt2 in range(2000):
        if n_list[cnt1][cnt2] == 1:
            x_list.append(cnt2)
            y_list.append(cnt1)

x_list.sort()
y_list.sort()

if x_list and y_list:
    print((x_list[-1]-x_list[0]+1)*(y_list[-1]-y_list[0]+1))
else: print(0)
