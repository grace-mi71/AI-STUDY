n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
n_list=[[0,0,'N'] for _ in range(200000)] 
OFFSET=100000
here=OFFSET
result=[0,0,0]
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

for i in range(n):
    if dir[i] == 'L':
        for _ in range(x[i]):
            n_list[here][0]+=1
            if n_list[here][0]>=2 and n_list[here][1]>=2: n_list[here][2]='G'
            elif n_list[here][2]!='G': n_list[here][2]='W'
            here-=1
        here+=1
    elif dir[i]=='R':
        for _ in range(x[i]):
            n_list[here][1]+=1
            if n_list[here][0]>=2 and n_list[here][1]>=2: n_list[here][2]='G'
            elif n_list[here][2]!='G': n_list[here][2]='B'
            here+=1
        here-=1

for color in n_list:
    if color[2]=='W': result[0]+=1
    elif color[2]=='B': result[1]+=1
    elif color[2]=='G': result[2]+=1

print(*result)
