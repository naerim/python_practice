
#### 다시 풀어보기

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    # 누적 합보다 화폐 단위가 클 경우 그 사이에 만들 수 없는 수가 존재한다.
    if target < x:
        break
    target += x

print(target)

####################################