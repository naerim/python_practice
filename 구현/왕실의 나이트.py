current = input()

result = 0
x = int(ord(current[0]) - 96)
y = int(current[1])

dx = [2, 2, 1, -1, -2, -2, 1, -1]
dy = [-1, 1, 2, 2, -1, 1, -2, -2]

for i in range(len(dx)):
    rx = x + dx[i]
    ry = y + dy[i]
    if rx < 1 or rx > 8 or ry < 1 or ry > 8:
        continue
    result += 1
    
print(result)
    
