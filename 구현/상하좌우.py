n = int(input())
array = list(input().split())

x = 1
y = 1
for i in array:
    if i == 'R':
        y += 1
    elif i == 'L':
        y -= 1
    elif i == 'U':
        x -= 1
    elif i == 'D':
        x += 1
    
    if y < 1:
        y = 1
    elif y > n:
        y = n
    
    if x < 1:
        x = 1
    elif x > n:
        x = n

####################################
# 책 풀이
n = int(input())
x,y = 1,1
plans = input().split

# L, R, U, D에 따른 이동 방햘
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny

print(x, y)