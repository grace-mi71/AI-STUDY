N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

handshakes.sort() # 튜플 정렬
N_list=[0]*(N+1) # 0~N 까지 개발자들 리스트
N_infect=[0]*(N+1) #감염됐는지 여부 개발자들 리스트
N_list[P]=K #P번 개발자에게 K번 감염 횟수 초기화
N_infect[P]=1 #P번 개발자 감염 양성 초기화

for i in range(len(handshakes)):
    if N_infect[handshakes[i][1]]==1 and N_infect[handshakes[i][2]]==0:
        if N_list[handshakes[i][1]]>0:
            N_infect[handshakes[i][2]]=1
            N_list[handshakes[i][2]]=K
            N_list[handshakes[i][1]]-=1
    elif N_infect[handshakes[i][1]]==0 and N_infect[handshakes[i][2]]==1:
        if N_list[handshakes[i][2]]>0:
            N_infect[handshakes[i][1]]=1
            N_list[handshakes[i][1]]=K
            N_list[handshakes[i][2]]-=1
    elif N_infect[handshakes[i][1]]==1 and N_infect[handshakes[i][2]]==1:
        if N_list[handshakes[i][1]]>0:
            N_list[handshakes[i][1]]-=1
        if N_list[handshakes[i][2]]>0:
            N_list[handshakes[i][2]]-=1

del N_infect[0]

answer=''.join(map(str, N_infect))
print(answer)
    

# Please write your code here.