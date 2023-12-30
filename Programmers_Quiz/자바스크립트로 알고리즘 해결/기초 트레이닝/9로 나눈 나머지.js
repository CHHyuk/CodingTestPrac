function solution(number) {
    sum = 0
    for (let i = 0; i < number.length; i++) {
        sum = sum + Number(number[i])
    }
    return sum % 9
}