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