function solution(my_string, overwrite_string, s) {
    
    let answer = ''
    
    for (let i = 0; i < my_string.length; i++) {
        if (i >= Number(s) && i - Number(s) < overwrite_string.length) {
            answer = answer + overwrite_string[i-Number(s)]
        } else {
            answer = answer + my_string[i]
        }
    }

    return answer 
}