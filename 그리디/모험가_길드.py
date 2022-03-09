n = int(input())
arr = list(map(int, input().split()))

# 숫자가 큰 순으로 정렬
arr.sort(reverse=True)

count = 0
i = 0
# 숫자 인덱스만큼 건너뛰기
while i < n:
    i = i + arr[i]
    count += 1
    
print(count)

####################################
# 다른 답안
arr.sort()

result = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in arr: # 공포도 낮은 것부터 확인
    count += 1 # 현재 그룹에 해당 모함가를 포함시킴
    if count >= i: # 현재 그룹의 모험가 수가 현재의 공포도 이상이면, 그룹 결성
        result += 1
        count = 0
print(result)