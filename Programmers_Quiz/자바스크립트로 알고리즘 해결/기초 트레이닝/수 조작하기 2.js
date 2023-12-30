function solution(numLog) {
    answer = ''
    for (let i = 1; i < numLog.length; i++) {
        if (numLog[i] - numLog[i-1] == 1) {
            answer = answer + 'w'
        } else if (numLog[i] - numLog[i-1] == -1) {
            answer = answer + 's'
        } else if (numLog[i] - numLog[i-1] == 10) {
            answer = answer + 'd'
        } else {
            answer = answer + 'a'
        }
    }
    return answer
}