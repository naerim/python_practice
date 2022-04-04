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
print(num) # >> 숫자가 없을때도 고려해줘야 함..!

####################################
# 책 풀이

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))
    
# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
# join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수