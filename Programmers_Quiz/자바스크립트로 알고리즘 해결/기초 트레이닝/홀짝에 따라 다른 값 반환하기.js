function conditionalIntegerSum(number) {
    if (number % 2 == 0 ) {
        let sum = 0
        for (let i = number; i > 0; i = i - 2) {
            sum = sum + i ** 2
        }
        return sum
    } else {
        let sum = 0
        for (let i = number; i > 0; i = i - 2) {
            sum = sum + i
        }
        return sum
    }
}

function solution(n) {
    return conditionalIntegerSum(n)
}