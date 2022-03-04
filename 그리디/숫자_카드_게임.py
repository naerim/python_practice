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