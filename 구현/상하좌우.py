n = int(input())
array = list(input().split())

x = 1
y = 1
for i in array:
    if i == 'R':
        y += 1
    elif i == 'L':
        y -= 1
    elif i == 'U':
        x -= 1
    elif i == 'D':
        x += 1
    
    if y < 1:
        y = 1
    elif y > n:
        y = n
    
    if x < 1:
        x = 1
    elif x > n:
        x = n

