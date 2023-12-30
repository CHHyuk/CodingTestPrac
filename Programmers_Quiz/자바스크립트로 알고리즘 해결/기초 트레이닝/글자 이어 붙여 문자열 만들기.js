function solution(my_string, index_list) {
    
    answer = ''

    for (i = 0; i < index_list.length; i++) {
        answer = answer + my_string[index_list[i]]
    }
    
    return answer 
}