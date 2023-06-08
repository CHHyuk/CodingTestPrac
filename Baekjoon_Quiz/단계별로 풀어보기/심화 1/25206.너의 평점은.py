sum = 0
count = 0

grade =['A+','A0','B+','B0','C+','C0','D+','D0']
grade_score = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0]

while True:
    try:
        score = input()
        check = score[-6:]
        if check[-2:] in grade:
            sum += grade_score[grade.index(check[-2:])] * float(check[:3])
            count += float(check[:3])
        elif score[-1] == 'F':
            count += float(check[:3])
            continue
    except:
        break

print(sum/count)