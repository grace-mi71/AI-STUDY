n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

x=0
y=0
dx=[1,-1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    if dir[i]=='E':
        for _ in range(dist[i]):
            x+=dx[0]
            y+=dy[0]

    elif dir[i]=='W':
        for j in range(dist[i]):
            x+=dx[1]
            y+=dy[1]

    elif dir[i]=='S':
        for j in range(dist[i]):
            x+=dx[2]
            y+=dy[2]

    elif dir[i]=='N':
        for j in range(dist[i]):
            x+=dx[3]
            y+=dy[3]

print(x, y)