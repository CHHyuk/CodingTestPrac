"""
Lv.0 중복된 숫자 개수
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
"""


def solution(array, n):
    return array.count(n) # array 라는 리스트에 .count(n) 은 n의 갯수가 몇개인지를 나타내어줌