def solution(s):
    # 이진 변환 카운트, 제거된 0의 카운트
    binary_count, zero_count = 0, 0
    # 주어진 s를 쪼개서 리스트로 저장
    new_s = list(map(str, s))
    # 이진 변환의 결과가 1이 될 때까지 반복
    # len(new_s) = 1 이라면, new_s[0] = 1
    while len(new_s) > 1:
        # 임시 저장 리스트
        temp = []
        # new_s를 순회하면서
        for c in new_s:
            # 0인 경우, zero_count를 증가하면서 삭제(저장 X)
            if c == "0":
                zero_count += 1
            # 1인 경우, temp에 추가
            else:
                temp.append(c)
        # 0이 제거된 후의 길이
        length = len(temp)
        # length를 2진수로 변환 후, new_s에 저장
        new_s = list(bin(length))[2:]
        # 이진 변환 카운트 증가
        binary_count += 1
    return [binary_count, zero_count]