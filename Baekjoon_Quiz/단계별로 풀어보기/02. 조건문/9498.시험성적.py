"""
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
"""

a = int(input())

if a >= 90 and a <= 100:
    print("A")
elif a >= 80 and a < 90:
    print('B')
elif a >= 70 and a < 80:
    print('C')
elif a >= 60 and a < 70:
    print('D')
elif a < 60:
    print('F')