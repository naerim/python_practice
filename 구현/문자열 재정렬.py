from multiprocessing import Array


s = input()

num = 0
arr = []
for i in range(len(s)):
   if (s[i] >= '0' and s[i] <= '9'):
       num += int(s[i])
   else:
       arr.append(s[i])

new_arr = sorted(arr)

for i in new_arr:
    print(i, end='')
print(num)
