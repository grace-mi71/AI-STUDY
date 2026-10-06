from collections import deque

A = input()
queue = deque()
cnt=0

for ch in A:
    queue.append(ch)

while(1):
    if queue[0]==')':
        queue.popleft()
    else:
        break

for i in range(len(queue)):
    if queue[i]=='(':
        for j in range(i, len(queue)):
            if queue[j]==')':
                cnt+=1

print(cnt)