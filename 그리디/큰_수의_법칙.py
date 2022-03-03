n = 5
m = 8
k = 3
arr = [2,4,5,4,6]
# n = 5
# m = 7
# k = 2
# arr = [3,4,3,4,3]
result = 0

# m과 k의 관계 - 나머지만큼 숫자 인덱스 필요
r = m % k

# 배열 큰 순으로 정렬
arr.sort(reverse=True)

# 제일 큰 숫자 * m에서 r만큼 뺀 값 더하기
result = arr[0] * (m-r)

# 두번째로 큰 숫자 * r
result +=  arr[1] * r

####################################

# n,m,k를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second # 두번재로 큰 수 더하기
print(result)