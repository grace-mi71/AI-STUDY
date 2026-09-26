n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

robot_a_arr=[]
robot_b_arr=[]

robot_a_arr.append(0)
robot_b_arr.append(0)

a_here=0
b_here=0

for i in range(n):
    if d[i]=='L':
        for _ in range(t[i]):
            a_here-=1
            robot_a_arr.append(a_here)
    elif d[i]=='R':
        for _ in range(t[i]):
            a_here+=1
            robot_a_arr.append(a_here)

for i in range(m):
    if d_b[i]=='L':
        for _ in range(t_b[i]):
            b_here-=1
            robot_b_arr.append(b_here)
    elif d_b[i]=='R':
        for _ in range(t_b[i]):
            b_here+=1
            robot_b_arr.append(b_here)

final_length_min=min(len(robot_a_arr), len(robot_b_arr))
final_length_max=max(len(robot_a_arr), len(robot_b_arr))
cnt=0

for i in range(1, final_length_min):
    if robot_a_arr[i] == robot_b_arr[i]:
        if robot_a_arr[i-1] != robot_b_arr[i-1]:
            cnt+=1

for j in range(final_length_min, final_length_max):
    if len(robot_a_arr)==final_length_max:
        if robot_a_arr[j] == robot_b_arr[-1]:
            if robot_a_arr[j-1] != robot_b_arr[-1]:
                cnt+=1
    elif len(robot_b_arr)==final_length_max:
        if robot_b_arr[j]==robot_a_arr[-1]:
            if robot_b_arr[j-1] != robot_a_arr[-1]:
                cnt+=1

print(cnt)

