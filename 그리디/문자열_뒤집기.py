S = list(map(int, input().split()))

result = 0
count0 = 0
count1 = 0
prev = 0
next = 0

# 0과 1의 갯수 구하기
for i in S:
    if i == 0:
        count0 += 1
    else:
        count1 += 1
        
# 비교
if count0 >= count1:
    prev = 0
    next = 1
else:
    prev = 1
    next = 0
     
# 숫자가 바뀌는 지점 count하기 
for i in range(1, len(S)):
    if S[i-1] == prev and S[i] == next:
        result +=1
        
print(result)