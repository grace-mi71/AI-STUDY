n = int(input())

MAX = 200000
OFFSET = 100000

# 0: 칠하지 않음
# 1: 흰색
# 2: 검은색
# 3: 회색
color = [0] * MAX

white_cnt = [0] * MAX
black_cnt = [0] * MAX

here = OFFSET

for _ in range(n):
    x, direction = input().split()
    x = int(x)

    if direction == 'L':
        for i in range(x):
            pos = here - i

            # 이미 회색이면 색은 바뀌지 않음
            if color[pos] == 3:
                continue

            white_cnt[pos] += 1

            if white_cnt[pos] >= 2 and black_cnt[pos] >= 2:
                color[pos] = 3
            else:
                color[pos] = 1

        # 마지막으로 칠한 위치
        here -= x - 1

    else:  # R
        for i in range(x):
            pos = here + i

            if color[pos] == 3:
                continue

            black_cnt[pos] += 1

            if white_cnt[pos] >= 2 and black_cnt[pos] >= 2:
                color[pos] = 3
            else:
                color[pos] = 2

        here += x - 1


white = 0
black = 0
gray = 0

for c in color:
    if c == 1:
        white += 1
    elif c == 2:
        black += 1
    elif c == 3:
        gray += 1

print(white, black, gray)