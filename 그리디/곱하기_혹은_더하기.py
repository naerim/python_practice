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