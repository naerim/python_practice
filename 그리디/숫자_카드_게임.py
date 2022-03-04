n,m = map(int, input().split())
# 배열 초기화
arr = [0 for _ in range(n)]

# 배열 입력 받기
for i in range(n):
    arr[i] = list(map(int, input().split()))

min = [0] * n # 각 행의 작은 수를 저장해놓는 배열
result = 0
for i in range(n):
    for j in range(m):
        if j == m-1:
            break
        if arr[i][j+1] <= arr[i][j]:
            min[i] = arr[i][j+1]
    if i == 0:
        result = min[i]
    elif i == m:
        break
    else:
        if min[i] > min[i-1]: # 행의 최솟값이 자신보다 크면 바꾸기
            result = min[i]

####################################
## min() 함수를 이용하는 답안
n,m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)

####################################
## 2중 반복문 구조를 이용하는 답안
n,m = map(int, input().split())

result = 0
# 한 줄 씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)