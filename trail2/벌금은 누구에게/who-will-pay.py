N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
result=-1
student_score=[0]*N

for i in range(M):
    student_score[student[i]-1]+=1
    if student_score[student[i]-1]>=K:
        result=student[i]
        print(result)
        break

if result==-1:
    print(result)
