n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs=[1,0,-1,0]
dys=[0,-1,0,1]

x=0
y=0
answer=0
cnt=0

def in_range(x,y,n):
    return 0<=x and x<n and 0<=y and y<n

for i in range(n):
    for j in range(n):
        x,y=j,i
        for dx,dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy
            if in_range(nx,ny,n) and grid[nx][ny]==1:
                cnt+=1
            nx, ny = x, y
        if cnt>=3:
            answer+=1
        cnt=0

print(answer)