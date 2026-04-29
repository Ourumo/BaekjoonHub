def solution(bandage, health, attacks):
    # bandage 분리
    b_time, b_hps, b_bonus = bandage
    
    # attacks를 딕셔너리 형태로 변환 | 마지막 공격 시간 저장
    a_dic = {}
    full_time = 0
    for a in attacks:
        a_dic[a[0]] = a[1]
        full_time = max(full_time, a[0])
    
    # 공격 및 회복 (메인)
    bonus_cnt = 0
    max_health = health
    for i in range(1, full_time + 1):
        # 공격 처리
        dmg = a_dic.get(i)
        if dmg:
            health -= dmg
            bonus_cnt = 0
        # 회복 처리
        else:
            health += b_hps
            bonus_cnt += 1
            
            # 시전에 성공하면 추가 회복
            if bonus_cnt == b_time:
                health += b_bonus
                bonus_cnt = 0
            
            # 최대 체력을 초과한 경우 체력을 최대 체력으로
            health = min(health, max_health)
        
        # 생존 여부
        if health <= 0:
            return -1
        
    return health