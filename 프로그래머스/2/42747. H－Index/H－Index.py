def solution(citations):
    # 조건 정리
    # 1. 전체 중, x 이상의 값이 x개 이상
    # 2. 전체 중, x 미만의 값이 x개 이하

    # citations 오름차순 정렬
    citations.sort()
    # 결과를 저장할 변수
    result = 0

    for c in range(10000):
        # 1. 전체 중, x 이상의 값이 x개 이상
        condition1 = len(list(filter(lambda x: x >= c, citations))) >= c
        # 2. 전체 중, x 미만의 값이 x개 이하
        condition2 = len(list(filter(lambda x: x < c, citations))) <= c

        # (조건1 and 조건2)가 False면 탈출
        if not (condition1 and condition2):
            break

        # (조건1 and 조건2)가 True면 결과 저장
        result = c

    return result