function solution(rny_string) {
    answer = ''
    for (let i = 0; i < rny_string.length; i++) {
        if (rny_string[i] == 'm') {
            answer = answer + 'rn'
        } else {
            answer = answer + rny_string[i]
        }
    }
    return answer
}