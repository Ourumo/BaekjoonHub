# bfs
from collections import deque

def solution(begin, target, words):
    # 사용된 words 저장하는 list, words의 길이, 결과 저장
    used_words, len_word, result = [False] * len(words), len(target), 0
    d = deque() # bfs를 위한 deque | (word, count)
    d.append((begin, 0)) # 기본값으로 (begin, 0)

    while d:
        word, c = d.popleft()

        # 현재 변환된 word가 taget과 같다면 완료 = 최소 단계
        if target == word:
            result = c
            break

        # words를 순회하면서 변환이 가능한 지 비교
        for i in range(len(words)):
            count = 0
            # 이미 변환한 적 있는 word면 continue
            if used_words[i] == True:
                continue

            # 각 문자 비교
            for j in range(len_word):
                if not word[j] == words[i][j]:
                    count += 1

            # count가 1 = 변환 가능
            if count == 1:
                d.append((words[i], c + 1))
                used_words[i] = True

    return result