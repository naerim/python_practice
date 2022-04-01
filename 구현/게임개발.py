from calendar import c


size = list(map(int, input().split()))
character = list(map(int, input().split()))

place = [] # 맵
# 맵의 크기만큼 입력받기
for i in range(size[0]):
    place.append(list(map(int, input().split())))
        
# 바라보고 있는 방향 기준 계산
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
current = character[2] # 현재 바라보고 있는 방향

result = 0
x = character[0]
y = character[1]

# 캐릭터 움직이기


# 현재 방향 기준으로 반시계방향 확인하기
def check_direction(current):
    count = 1
    while count < 5:
        if current > 3:
            current = 0
        next = place[dx[current]][dy[current]] # 다음이 바디인지 육지인지
        if next != 0:
            # 육지이면 이동
            x += dx
            y += dy
            result += 1
            break
        else: 
            # 바다면 방향 변경
            current += 1
        count += 1
    return current