S = list(map(int, input().split()))
result = 0

for i in range(0, len(S)):
    # 첫번째 인덱스는 더하기
    if i == 0:
        result += S[i]
        continue
    # 앞의 숫자가 0이거나 1이면 더하기
    if S[i-1] == 0 or S[i-1] == 1:
        result += S[i]
    else:
        result *= S[i]
        
print(result)


data = input() # 첫 번째 문자를 숫자로 변경하여 대입 
result = int(data[0]) 
for i in range(1, len(data)): 
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행 
    num = int(data[i]) 
    if num <= 1 or result <= 1: 
        result += num 
    else: 
        result *= num 
print(result)
