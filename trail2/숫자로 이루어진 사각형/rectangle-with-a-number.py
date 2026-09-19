n = int(input())

def write_rect(n):
    num=1
    for i in range(n):
        for j in range(n):
            print(num, end=' ')
            num=num%9+1
        print()

write_rect(n)