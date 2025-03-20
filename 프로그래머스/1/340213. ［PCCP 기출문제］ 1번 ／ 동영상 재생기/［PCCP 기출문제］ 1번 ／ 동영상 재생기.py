# mm에서 ss로 단위 변경
def mm_to_ss(t):
    tmp_mm, tmp_ss = map(int, t.split(':'))
    return tmp_mm * 60 + tmp_ss


# ss에서 mm으로 단위 변경
def ss_to_mm(t):
    tmp_mm, tmp_ss = t // 60, t % 60

    mm = "0" + str(tmp_mm) if tmp_mm < 10 else str(tmp_mm)
    ss = "0" + str(tmp_ss) if tmp_ss < 10 else str(tmp_ss)

    return mm + ":" + ss


# pos가 op_start와 op_end 사이에 있는지 확인
def pos_in_op(p, op_s, op_e):
    return op_e if p >= op_s and p <= op_e else p


def solution(video_len, pos, op_start, op_end, commands):
    video_len_to_s = mm_to_ss(video_len) # video_len 단위 변경
    pos_to_s = mm_to_ss(pos) # pos 단위 변경
    op_start_to_s = mm_to_ss(op_start) # op_start 단위 변경
    op_end_to_s = mm_to_ss(op_end) # op_end 단위 변경

    # pos가 op_start와 op_end 사이에 있는지 확인 / 최초
    pos_to_s = pos_in_op(pos_to_s, op_start_to_s, op_end_to_s)

    # commands의 크기만큼 반복
    for c in commands:
        if c == "next": # commands == next
            pos_to_s += 10
        else: # commands == prev
            pos_to_s -= 10
            
        # pos가 음수인지 확인 / 반복
        if pos_to_s < 0:
            pos_to_s = 0

        # pos가 op_start와 op_end 사이에 있는지 확인 / 반복
        pos_to_s = pos_in_op(pos_to_s, op_start_to_s, op_end_to_s)

        # pos가 video_len보다 큰지 확인 / 반복
        if pos_to_s > video_len_to_s:
            pos_to_s = video_len_to_s

    return ss_to_mm(pos_to_s)