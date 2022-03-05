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
    # n이 k보다 작을 때 고려
    if n > k:
        result = divide_num(n) + remain
    else:
        result = remain - 1 # 1 빼주기 <<
print(result)

####################################

n,k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)