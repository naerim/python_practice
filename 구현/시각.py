import string
from unittest import result


h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있으면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(h)

# 완전 탐색 : 경우의 수를 모두 검사해보는 방법
# 확인해야할 전체 데이터의 개수가 100만 개 이하일 때 완전 탐색 사용하기