# 베스트엘범 xxxxxxxxxxxxxxxx

def solution(genres, plays):
    gp_dict_1 = {}
    gp_dict_2 = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in gp_dict_1:
            gp_dict_1[genres[i]] = plays[i]
        elif genres[i] in gp_dict_1 and genres not in gp_dict_2:
            if gp_dict_1[genres[i]] >= plays[i]:
                gp_dict_2[genres[i]] = plays[i]
            else:
                gp_dict_2[genres[i]] = gp_dict_1[genres[i]]
                gp_dict_1[genres[i]] = plays[i]
        elif genres[i] in gp_dict_1 and genres[i] in gp_dict_2:
            if gp_dict_1[genres[i]] >= plays[i]:
                1

solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])