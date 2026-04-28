# 1. 총 개수가 가장 높은 장르
# 2. 그 장르 중 많이 재생된 노래
# 3. 고유 번호가 낮은 노래
def solution(genres, plays):
    result = []

    # 딕셔너리 선언
    total_dic = {}
    genre_play_dic = {}

    # 딕셔너리에 저장
    for i in range(len(plays)):
        genre = genres[i]
        play = plays[i]

        if not total_dic.get(genre):
            total_dic[genre] = play
            genre_play_dic[genre] = [[i, play]]
        else:
            total_dic[genre] += play
            genre_play_dic[genre].append([i, play])

    sorted_key = sorted(total_dic, key=lambda x: (-total_dic[x]))
    for k in sorted_key:
        sorted_value = sorted(genre_play_dic[k], key=lambda x: (x[1], -x[0]))
        result.append(sorted_value[-1][0])
        if len(sorted_value) > 1:
            result.append(sorted_value[-2][0])

    return result
        