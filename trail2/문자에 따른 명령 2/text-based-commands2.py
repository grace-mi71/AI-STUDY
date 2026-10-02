dirs = input()

dirs_num=3 #북쪽 바라보도록
dx=[1,0,-1,0]
dy=[0,-1,0,1]

x=0
y=0

dirs_command=list(dirs)

for i in dirs_command:
    if i=='L':
        dirs_num=(dirs_num+3)%4
    if i=='R':
        dirs_num=(dirs_num+1)%4
    if i=='F':
        x=x+dx[dirs_num]
        y=y+dy[dirs_num]

print(x,y)
