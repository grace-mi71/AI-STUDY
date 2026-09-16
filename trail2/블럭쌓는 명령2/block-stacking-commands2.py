n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

blocks=[0]*(n+1)

for i in range(k):
    for j in range(commands[i][0], commands[i][1]+1):
        blocks[j]+=1

print(max(blocks))

# Please write your code here.