# 로그인 성공?

def solution(id_pw, db):
    answer = ''
    for i in range(len(db)):
        if id_pw == db[i]:
            answer = "login"
        elif id_pw[0] == db[i][0] and id_pw[1] != db[i][1]:
            answer = 'wrong pw'
    
    if answer != "login" and answer != 'wrong pw':
        answer = 'fail'
    
    return answer





solution(["meosseugi", "1234"])