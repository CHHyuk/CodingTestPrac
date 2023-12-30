function solution(num_str) {
    answer = 0
    
    for (let i = 0; i < num_str.length; i++) {
        answer = answer + Number(num_str[i])
    }

    return answer
}