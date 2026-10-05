n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx=[1,0,0,-1]
dy=[0,1,-1,0]

mapping={
    'R':0,
    'D':1,
    'U':2,
    'L':3
}

map_list=[[0] * (n+2) for _ in range(n+2)]
move_dir=mapping[d]

for i in range(1,n+1):
    for j in range(1,n+1):
        map_list[i][j]=1

for i in range(t):
    if map_list[r+dy[move_dir]][c+dx[move_dir]]==1:
        r=r+dy[move_dir]
        c=c+dx[move_dir]
    elif map_list[r+dy[move_dir]][c+dx[move_dir]]==0:
        move_dir=3-move_dir

# print(map_list)
print(r,c)

