function solution(my_string, alp) {
    answer = ''
    
    for (i = 0; i < my_string.length; i++) {
        if (my_string[i] == alp) {
            answer = answer + my_string[i].toUpperCase()
        } else {
            answer = answer + my_string[i]
        }
    }
    return answer 
}