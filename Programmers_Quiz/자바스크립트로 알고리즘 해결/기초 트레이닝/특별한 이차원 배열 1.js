function solution(n) {
    answer = []
    while (answer.length < n) {
        temp = []
        for (let i = 0; i < n; i++) {
            if (answer.length == i) {
                temp.push(1)
            } else {
                temp.push(0)
            }
        }
        answer.push(temp)
    }
    return answer
}