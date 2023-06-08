"""
Lv.0 배열의 평균값
정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
"""


def solution(numbers):
    answer = sum(numbers) / len(numbers) # sum() : 리스트의 값을 모두 더함, len() : 리스트 항목의 갯수
    return answer