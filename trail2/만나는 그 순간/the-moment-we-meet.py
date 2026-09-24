n, m = map(int, input().split())

arr_A=[]
A_here=0
arr_B=[]
B_here=0

result=-1

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))


for i in range(n):
    for j in range(t[i]):
        if d[i]=='R':
            A_here+=1
        else:
            A_here-=1
        arr_A.append(A_here)

for i in range(m):
    for j in range(t2[i]):
        if d2[i]=='R':
            B_here+=1
        else:
            B_here-=1
        arr_B.append(B_here)
        

for i in range(sum(t)):
    if arr_A[i]==arr_B[i]:
        result=i+1
        break

print(result)
