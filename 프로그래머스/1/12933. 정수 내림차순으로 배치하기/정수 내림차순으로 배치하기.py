def solution(n):
    arr=[]
    for i in str(n):
        arr.append(i)
    arr.sort(reverse=True)
    sort_arr=list(map(str, arr))
    answer=''.join(sort_arr)
    return int(answer)