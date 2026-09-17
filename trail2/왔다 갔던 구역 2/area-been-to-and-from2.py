n = int(input())
x = []
dir = []
OFFSET=1000
n_list=[0]*2001
cnt=0

for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

here=OFFSET

for i in range(n):
    if dir[i]=='R':
        for _ in range(x[i]):
            n_list[here]+=1
            here+=1
    if dir[i]=='L':
        for _ in range(x[i]):
            here-=1
            n_list[here]+=1

for idx in range(len(n_list)):
    if n_list[idx]>=2:
        cnt+=1
print(cnt)
