n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)


a_arr=[]
a_here=0
b_arr=[]
b_here=0
result_arr=[]

a_arr.append(0)
b_arr.append(0)

for i in range(n):
    for j in range(t[i]):
        a_here+=v[i]
        a_arr.append(a_here)

for i in range(m):
    for j in range(t2[i]):
        b_here+=v2[i]
        b_arr.append(b_here)

for i in range(1, len(a_arr)):
    if a_arr[i]>b_arr[i]:
        result_arr.append('A')
    elif a_arr[i]<b_arr[i]:
        result_arr.append('B')

cnt=0
for i in range(1,len(result_arr)):
    if result_arr[i]!=result_arr[i-1]:
        cnt+=1
print(cnt)