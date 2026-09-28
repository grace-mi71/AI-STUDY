N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

a_here=[]
a_place=0
b_here=[]
b_place=0
result=[]

for i in range(N):
    for j in range(t[i]):
        a_place+=v[i]
        a_here.append(a_place)
for i in range(M):
    for j in range(t2[i]):
        b_place+=v2[i]
        b_here.append(b_place)

for i in range(sum(t)):
    if a_here[i]==b_here[i]:
        result.append('C')
    if a_here[i]>b_here[i]:
        result.append('A')
    if a_here[i]<b_here[i]:
        result.append('B')
cnt=0

for i in range(1, len(result)):
    if result[i]!=result[i-1]:
        cnt+=1
# print(result)
print(cnt+1)