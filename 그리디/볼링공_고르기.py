N,M = map(int, input().split())
K = list(map(int, input().split()))

result = 0;
for i in range(0, len(K)):
    for j in range(i+1, len(K)):
        # 같지 않으면 더하기
        if K[i] != K[j]:
            result += 1
        else:
            continue
print(result)
    