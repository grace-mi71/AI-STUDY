n, m = map(int, input().split())

def gcd(n,m):
    while m>0:
        n,m=m,n%m
    print(n)

gcd(n,m)
# Please write your code here.