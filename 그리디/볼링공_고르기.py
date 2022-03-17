N,M = map(int, input().split())
K = list(map(int, input().split()))

result = 0;
for i in range(0, len(K)):
    for j in range(i+1, len(K)):
        # 같지 않으면 더하기
        if K[i] != K[j]:
            result += 1
        else:
            continue
print(result)
    
####################################
# 위의 코드는 시간초과 나는듯?
n,m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게 담기
array = [0] * 11

# 각 무게에 해당하는 볼링공의 개수 카운트
for x in data:
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] # 무게가 1인 볼링공의 개수 재외(A가 선택할 수 있는 갯수)
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기