function solution(myString) {
    answer = myString.split('x').filter(item => item !== '');
    return answer.sort()
}