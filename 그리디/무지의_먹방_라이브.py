def solution(food_times, k):
    max = 0 # food_times 값들을 모두 더한 값
    for i in food_times:
        max += i
    
    num = len(food_times)
    i = 0
    count = 0 # 무지가 음식을 먹은 시간
    
    while count <= max: # 총 음식을 먹은 시간이 max보다 작을때까지만 반복
        if i == num: # 인덱스가 배열 길이보다 커지면 다시 0으로 바꾸기
            i = 0
        # print("i : " + str(i))
        # print("food : " + str(food_times))
        if food_times[i] == 0:
            i += 1
            if count == max: # 더 이상 섭취해야할 음식이 없을 때
                return -1
            continue
        else:
            if count == k: # 음식을 먹은 시간이 k랑 같으면 멈추기
                break
            food_times[i] -= 1
            count += 1
            i += 1
    return i + 1

array = [3,1,2]
print(solution(array, 8))