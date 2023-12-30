function solution(my_string, parts) {
    answer = ''
    for(let i = 0; i < parts.length; i++) {
        answer = answer + my_string[i].slice(parts[i][0],parts[i][1]+1)
    }
    return answer
}