function solution (my_string, n) {
    let answer = ''
    const index = my_string.length - n
    for (let i = index; i < my_string.length; i++) {
        answer = answer + my_string[i]
    }

    return answer 
}