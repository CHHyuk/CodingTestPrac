# 신고 결과 받기

def solution(id_list, report, k):
    check_report = {id_list[i] : 0 for i in range(len(id_list))}
    check_id = {id_list[i] : 0 for i in range(len(id_list))}
    check = []
    result = []
    report = list(set(report))
    for i in range(len(report)):
        report[i] = report[i].split()
        check_report[report[i][1]] += 1
    for key,value in check_report.items():
        if value >= k:
            check.append(key)
    for i in range(len(report)):
        if report[i][1] in check:
            check_id[report[i][0]] += 1
    for key, value in check_id.items():
        result.append(value)
    return result
    

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)