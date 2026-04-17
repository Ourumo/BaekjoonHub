# HH:MM -> MMMM
def parseMinutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

# 퇴장 처리 함수
def out(num, time, dict_a, dict_b):
    if not dict_b.get(num):
                dict_b[num] = time - dict_a[num]
    else:
        dict_b[num] += time - dict_a[num]

def caculate(b_time, b_fee, a_time, a_fee, d, keys):
    result = []
    for k in keys:
        temp_time = d[k]
        temp_fee = 0
        # 기본 시간보다 작은 경우
        if b_time >= d[k]:
            result.append(b_fee)
        else:
            temp_time -= b_time
            temp_fee += b_fee
            temp_q = temp_time // a_time
            temp_r = temp_time % a_time
            if not temp_r == 0:
                temp_q += 1
            temp_fee += temp_q * a_fee
            result.append(temp_fee)
    return result

def solution(fees, records):
    # fees 분리
    base_time, base_fee, add_time, add_fee = map(int, fees)

    # records 분리
    d_list = {}
    d_time = {}

    for r in records:
        time, car_num, in_out = map(str, r.split())
        time = parseMinutes(time)

        # 입장 처리
        if in_out == "IN":
            d_list[car_num] = time
        # 퇴장 처리
        else:
            out(car_num, time, d_list, d_time)
            d_list.pop(car_num)

    # 남아있는 차 정리
    last_time = parseMinutes("23:59")
    for k in d_list.keys():
        out(k, last_time, d_list, d_time)

    # 계산 과정
    sorted_d_time_keys = sorted(d_time)
    # parameter = 기본 시간, 기본 요금, 단위 시간, 단위 요금, d_time, 정렬된 d_time 키들
    return caculate(base_time, base_fee, add_time, add_fee, d_time, sorted_d_time_keys)