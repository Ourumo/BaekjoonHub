def solution(triangle):
    # 초기화된 새로운 배열 dp 생성
    dp = [0] * len(triangle[-1])
    # dp에 초기값 저장
    dp[0] = triangle[0][0]
    # 이중 for문으로 dp에 값 추가 및 계산
    for i in range(1, len(dp)):
        temp = []
        for j in range(len(triangle[i])):
            # triangle[i][0]번은 dp[0]번의 값만 더할 수 있음
            if j == 0:
                temp.append(dp[j] + triangle[i][j])
                continue
            # 그 외의 경우
            temp.append(max(dp[j] + triangle[i][j], dp[j - 1] + triangle[i][j]))
        # dp에 값 업데이트
        for k in range(len(temp)):
            dp[k] = temp[k]
    return max(dp)