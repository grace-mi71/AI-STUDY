n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
OFFSET=100000
n_list=[0]*200000
here=OFFSET
result=[0]*2

for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

for i in range(n):
    if dir[i] == 'R':
        for _ in range(x[i]):
            n_list[here]='B'
            here+=1
        here-=1
    elif dir[i] == 'L':
        for _ in range(x[i]):
            n_list[here]='W'
            here-=1
        here+=1

for color in n_list:
    if color=='W':
        result[0]+=1
    elif color=='B':
        result[1]+=1
    else: continue

print(*result)
