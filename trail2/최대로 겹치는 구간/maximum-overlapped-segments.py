n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

n_list=[0]*200


for i in range(n):
    for j in range(segments[i][0]+100, segments[i][1]+100): #offset 설정. 문제에서 음수가 나오므로 범위를 미리 100을 더해서 0이상이 되도록 세팅
        n_list[j]+=1

print(max(n_list))

# Please write your code here.