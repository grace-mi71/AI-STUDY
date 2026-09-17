n = int(input())
x = []
dir = []
OFFSET=1000 #오프셋 설정 (음수 순서라는 건 배열에 존재할 수 없으므로)
n_list=[0]*2001 #R이면 오른쪽으로 가고 수직선 위 정수 사이 구간을 배열로 나타냈을 시, x과 x+1사이는 x이라고 표현하자.
cnt=0

for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

here=OFFSET #현 위치를 표현할 변수. 미리 OFFSET을 더해준다.

for i in range(n):
    if dir[i]=='R': #R이면 오른쪽으로 가고 5번째 줄에서 이야기했다시피 x값을 높여준다.
        for _ in range(x[i]):
            n_list[here]+=1
            here+=1
    if dir[i]=='L': #L이면 왼쪽으로 가고 먼저 현 위치를 1만큼 감소시키고 그 이후에 here위치의 배열 키값을 1 증가시킨다.
        for _ in range(x[i]): 
            here-=1
            n_list[here]+=1

for idx in range(len(n_list)):
    if n_list[idx]>=2:
        cnt+=1
print(cnt)
