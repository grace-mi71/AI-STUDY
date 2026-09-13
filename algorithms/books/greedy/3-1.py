#아래 코드가 나의 풀이

# import sys
# input=sys.stdin.readline().rstrip()

# N=int(input)
# count=0
# count=N//500
# N%=500
# count+=N//100
# N%=100
# count+=N//50
# N%=50
# count+=N//10
# N%=10

# print(count)

#문제풀이 해답

import sys
input=sys.stdin.readline().rstrip() 
n=int(input) #n값 입력 받기
count=0 #첫 동전의 개수(처음 개수를 셀때는 0개)

coin_types=[500,100,50,10] #동전 종류

for coin in coin_types: 
    count = count+n//coin #동전 종류 마다 큰 값으로 차례대로 나누어 최소한의 동전 개수 확보
    n%=coin #한번 나눈 후 나머지를 n에 저장하여 다음 동전의 값으로 계산

print(count)