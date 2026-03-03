import sys
input = sys.stdin.readline
n=int(input())
MOD=1234567891
word=input().strip()

result=0
r=1

for c in word: 
    alp_num=ord(c)-ord('a')+1
    result=(result + alp_num*r)%MOD
    r=(r*31)%MOD

print(result)