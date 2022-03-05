n,k = map(int, input().split())
result = 0

# 나머지
remain = n % k

# 몫이 1일때까지 나누는 함수
def divide_num(num):
    i = 0
    while True:
        if num == 1:
            break
        num /= k
        i += 1
    return i

# 나머지 값에 따라 계산
if remain == 0:
    result = divide_num(n)
else:
    n -= remain # n이 k에 나누어 떨어지게 만들기
    result = divide_num(n) + remain
print(result)