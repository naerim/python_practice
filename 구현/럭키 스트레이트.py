n = int(input())

n_str = str(n)
half = int(len(n_str) / 2)

left_sum = 0
right_sum = 0

for i in range(half):
    left_sum += int(n_str[i])
    
for i in range(half, len(n_str)):
     right_sum += int(n_str[i])
    
if left_sum == right_sum:
    print("LUCKY");
else:
    print("READY")
    
####################################
# 책 풀이

n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])
    
for i in range(length // 2, length):
    summary -= int(n[i])
    
if summary == 0:
    print("LUCKY");
else:
    print("READY")
    
# // : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함