def solution(record):
    uid_to_name = {}
    uid_order = []
    result = []

    for r in record:
        new_record = list(map(str, r.split(" "))) # [order, uid, (name)]
        if new_record[0] == "Enter": # Enter 처리
            uid_to_name[new_record[1]] = new_record[2]
            uid_order.append(f"{new_record[1]}|님이 들어왔습니다.")
        elif new_record[0] == "Leave": # Leave 처리
            uid_order.append(f"{new_record[1]}|님이 나갔습니다.")
        else: # Change 처리
            uid_to_name[new_record[1]] = new_record[2]

    # uid -> name 변환
    for n in uid_order:
        uid, order = map(str, n.split("|"))
        result.append(f"{uid_to_name[uid]}{order}")

    return result