n, m = map(int, input().split())

def gcd(n,m):
    while m>0:
        n,m=m,n%m
    return n

x=gcd(n,m)
result=x*(n//x)*(m//x)
print(result)


# Please write your code here.