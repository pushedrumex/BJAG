# Greedy

# 가장 먼 집부터 시작해서 최대한 배달하기
# 가장 먼 집부터 시작해서 최대한 수거하기
# Tip : 트럭이 가장 끝 집에 도착하면 오는 길에 택배를 배달하기 때문에 트럭에 있는 택배의 개수는 0개 -> 오는길에 배달, 돌아가는 길에 수거
# 수거한 빈 택배가 cap개가 되면 물류창고로 돌아가야함

def solution(cap, n, deliveries, pickups):
    answer = 0
    # 맨 끝집부터 시작
    delivery_idx, pickup_idx = n, n
    while n > 0:
        # 배달개수, 수거개수
        delivery, pickup = 0, 0
        
        # 맨 끝에 있는 집의 배달 또는 수거 개수가 0일 경우, 그 집까지 갈 필요 없음 
        while delivery_idx and deliveries[delivery_idx-1] == 0: delivery_idx -= 1
        while pickup_idx and pickups[pickup_idx-1] == 0: pickup_idx -= 1
        
        # 맨 끝에 있는 집의 배달 또는 수거 개수가 0이 아닐 경우, 그 집까지 가야함
        n = max(delivery_idx, pickup_idx)
        
        answer += n
        
        # 끝집에서부터 최대한 배달하기
        while delivery_idx and delivery < cap:
            delivery += deliveries[delivery_idx-1]
            delivery_idx -= 1
        if delivery > cap:
            delivery_idx += 1
            deliveries[delivery_idx-1] = delivery - cap
        
        # 끝집에서부터 최대한 수거하기
        while pickup_idx and pickup < cap:
            pickup += pickups[pickup_idx-1]
            pickup_idx -= 1
        if pickup > cap:
            pickup_idx += 1
            pickups[pickup_idx-1] = pickup - cap

    return answer*2 # 왕복거리
