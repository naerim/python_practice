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