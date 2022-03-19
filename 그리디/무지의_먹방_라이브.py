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

####################################
# 위의 코드는 정확도 100, 효율성 0

import heapq

def solution1(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 햔재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
    
# heapq
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & return

# sorted
# sorted(정렬할 데이터, key 파라미터)