function solution(n) {
    answer = [n]
    while (n > 1) {
        if (n % 2 == 0) {
            answer.push(n/2)
            n = n / 2
        } else {
            answer.push((3 * n) + 1)
            n = (3 * n) + 1
        }
    }
    return answer
}