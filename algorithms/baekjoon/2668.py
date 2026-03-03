import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
nxt=[0]*(n+1)
for i in range(1,n+1):
    nxt[i]=int(input())

visited=[False]*(n+1)
in_stack=[False]*(n+1)
stack=[]
answer=set()

def dfs(v):
    visited[v]=True
    in_stack[v]=True
    stack.append(v)

    next_node=nxt[v]
    if not visited[next_node]:
        dfs(next_node)
    elif in_stack[next_node]:
        idx=stack.index(next_node)
        for i in range(idx,len(stack)):
            answer.add(stack[i])

    stack.pop()
    in_stack[v]=False

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)

answer=sorted(answer)
print(len(answer))
for num in answer:
    print(num)
