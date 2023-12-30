function solution(my_string) {
    answer = []
    n = my_string.length - 1
    temp = ''
    while (answer.length != my_string.length) {
        temp = my_string[n] + temp
        n = n - 1
        answer.push(temp)
    }
    
    return answer.sort()
}