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
