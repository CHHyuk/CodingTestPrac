# 주차 요금 계산 xxxxxxxxxxxxxxxxxxxxxxx
import datetime

def solution(fees, records):
    temp = []
    time = 0
    for i in range(len(records)):
        if 'IN' in records[i]:
            temp.append(records[i][:10])
        elif 'OUT' in records[i]:
            for j in range(len(temp)):
                if records[i][6:10] in temp[j]:
                    time = datetime.datetime.strptime(records[i][0:5],'%H:%M') - datetime.datetime.strptime(temp[j][0:5],'%H:%M')
                    print(time)








solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])